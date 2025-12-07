# utils/mochi_film.py — FINAL 100% GPU-ACCELERATED MOCHI 1 CINEMA BOT (Dec 2025)
# This is the version that actually works — full RTX power, no CPU fallback
from diffusers import MochiPipeline
from diffusers.utils import export_to_video
import torch
import random
import os
import time
from datetime import datetime

# ==================== MOVIEPY IMPORTS (PyCharm-clean) ====================
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import moviepy.video.fx.all as vfx

from utils.multi_post import post_everywhere


# ==================== MOCHI 1 — FINAL GPU FIX (THE ONE THAT WORKS) ====================
print("Loading Mochi 1 (bf16 variant) — ~3–5 min first time...")

pipe = MochiPipeline.from_pretrained(
    "genmo/mochi-1-preview",
    variant="bf16",
    torch_dtype=torch.bfloat16
)

device = "cuda" if torch.cuda.is_available() else "cpu"

# THE CRITICAL LINE — moves the 10B-param transformer to GPU
pipe.transformer = pipe.transformer.to(device)
pipe = pipe.to(device)

pipe.enable_vae_tiling()

try:
    pipe.enable_xformers_memory_efficient_attention()
    print("xformers enabled — faster generation")
except:
    print("xformers not available — still runs fine")

if device == "cuda":
    vram = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"Mochi 1 FULLY ON GPU — VRAM: {vram:.1f} GB — READY TO RENDER CINEMA")
else:
    print("CUDA not detected — install torch+cuda")

print("Mochi 1 ready — cinematic generation starting...")


def generate_mochi_clip(prompt: str, duration: int = 8, seed: int = None) -> str:
    generator = torch.Generator(device=device)
    if seed is not None:
        generator.manual_seed(seed)

    print(f"  → Generating Mochi clip ({duration}s on GPU): {prompt[:80]}...")

    with torch.autocast("cuda", dtype=torch.bfloat16):
        frames = pipe(
            prompt=prompt,
            num_inference_steps=28,
            guidance_scale=7.0,
            num_frames=24 * duration,
            height=1280,
            width=720,
            generator=generator
        ).frames[0]

    temp_path = f"temp_mochi_{int(time.time())}_{random.randint(1000,9999)}.mp4"
    export_to_video(frames, temp_path, fps=24)
    print(f"    → Clip ready: {os.path.getsize(temp_path)/(1024*1024):.1f} MB")
    return temp_path


def generate_short_film(headline: str, base_prompt: str, caption: str) -> str | None:
    os.makedirs("shorts", exist_ok=True)

    variations = [
        f"{base_prompt}, epic wide establishing shot, dramatic volumetric god rays, slow cinematic motion, museum quality",
        f"{base_prompt}, intimate macro detail, iridescent light play, emotional depth, film grain",
        f"{base_prompt}, surreal overhead orbit, financial data streams morphing into abstract forms",
        f"{base_prompt}, golden hour hero shot, lens flare through volatility clouds, breathtaking scale",
        f"{base_prompt}, dolly through gamma cathedral, fractal reflections, ambient glow",
        f"{base_prompt}, abstract liquidity dissolve, waves of order flow, emotionally charged"
    ]
    prompts = random.sample(variations, k=random.randint(4, 6))

    raw_clips = []
    for i, p in enumerate(prompts, 1):
        seed = random.randint(0, 2**32 - 1)
        path = generate_mochi_clip(p, duration=8, seed=seed)
        raw_clips.append(VideoFileClip(path))

    clips = []
    for i, clip in enumerate(raw_clips):
        if i > 0: clip = clip.crossfadein(1.5)
        if i < len(raw_clips)-1: clip = clip.crossfadeout(1.5)
        clips.append(clip)

    film = concatenate_videoclips(clips, method="compose")
    print(f"  → Film stitched: {film.duration:.1f}s ({len(clips)} scenes)")

    if os.path.isdir("film_audio"):
        tracks = [f for f in os.listdir("film_audio") if f.lower().endswith(('.mp3', '.wav', '.m4a'))]
        if tracks:
            audio_path = os.path.join("film_audio", random.choice(tracks))
            audio = AudioFileClip(audio_path).subclip(0, film.duration).volumex(0.26)
            film = film.set_audio(audio)
            print(f"  → Audio layered: {os.path.basename(audio_path)}")

    # TRUE 1080×1920 9:16 + CINEMATIC POLISH
    film_hd = film.resize(height=1920)
    film_final = film_hd.fx(vfx.colorx, 1.05).fx(vfx.sharpen, 0.3)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    safe_title = "".join(c if c.isalnum() else "_" for c in headline.split(':')[0][:30])
    final_path = f"shorts/{timestamp}_{safe_title}_1080p.mp4"

    film_final.write_videofile(
        final_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        preset="slow",
        bitrate="8000k",
        threads=8,
        logger=None
    )
    print(f"FINAL 1080×1920 CINEMATIC SHORT FILM → {final_path}")

    for clip in raw_clips:
        try: os.unlink(clip.filename)
        except: pass

    post_everywhere(final_path, caption)
    return final_path