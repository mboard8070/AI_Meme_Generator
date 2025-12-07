# utils/flux_local.py — FINAL, WORKS ON EVERY WINDOWS MACHINE
import torch
from diffusers import FluxPipeline
from huggingface_hub import login
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

token = os.getenv("HF_TOKEN")
if token:
    login(token)

pipe = None

def load_flux_model():
    global pipe
    if pipe is None:
        try:
            pipe = FluxPipeline.from_pretrained(
                "black-forest-labs/FLUX.1-schnell",
                torch_dtype=torch.bfloat16,
                token=token,
                safety_checker=None,
                requires_safety_checker=False
            )

            # THIS LINE IS REQUIRED ON WINDOWS — DO NOT REMOVE
            if torch.cuda.is_available():
                pipe.enable_model_cpu_offload()          # GPU + smart offload = fast + stable
            else:
                pipe.to("cpu")                           # CPU-only fallback

            print("FLUX.1-SCHNELL LOADED SUCCESSFULLY — READY TO PUMP")
        except Exception as e:
            print(f"Flux load error: {e}")
            pipe = None
    return pipe

def generate_flux_image(prompt: str):
    model = load_flux_model()
    if not model:
        return None

    try:
        image = model(
            prompt,
            height=1024,
            width=1024,
            guidance_scale=0.0,
            num_inference_steps=4,
            generator=torch.Generator(device="cuda" if torch.cuda.is_available() else "cpu").manual_seed(int(datetime.now().timestamp()))
        ).images[0]

        os.makedirs("output", exist_ok=True)
        path = f"output/meme_{int(datetime.now().timestamp())}.jpg"
        image.save(path)
        print(f"FLUX MEME GENERATED → {path}")
        return path
    except Exception as e:
        print(f"Generation error: {e}")
        return None