import requests
import random

def generate_viral_flux_prompt():
    tickers = ["NVDA","TSLA","BTC","SPX","QQQ","SOL","AMD","MARA","HOOD","GME","AAPL","MSTR"]
    ticker = random.choice(tickers)

    vibes = [
        "market is in full euphoria, everything pumping",
        "crypto winter is back, blood on the streets",
        "FOMC just dropped the nuke",
        "gamma squeeze incoming",
        "retail getting absolutely rekt",
        "institutional accumulation phase",
        "weekend pump loading",
        "Elon just tweeted"
    ]

    template = f"""You are the most viral meme artist of 2025.
Create ONE extremely detailed, unhinged, maximalist Flux prompt about {ticker}.

Current vibe: {random.choice(vibes)}
Style: mix of Beeple, Pak, Refik Anadol, XCOPY, and 2017 crypto punk aesthetic
Mood: pure degen energy, diamond hands, paper hands burning, money printer go brrr

Include: laser eyes, apes in lambos, burning bears, federal reserve on fire, charts made of gold/neon, glitch effects, volumetric god rays, ultra dramatic lighting, money rain, diamond-encrusted everything

Make it so over-the-top it breaks Instagram. 8k, cinematic, award-winning.

Output ONLY the prompt. No quotes. Max 400 tokens."""

    # Using local Ollama (gemma2:27b or llama3.1:70b)
    try:
        r = requests.post("http://localhost:11434/api/generate", json={
            "model": "gemma2:27b-instruct-q6_k",
            "prompt": template,
            "stream": False,
            "options": {"temperature": 1.15, "top_p": 0.95}
        }, timeout=50)
        return r.json()["response"].strip().strip('"')
    except:
        # Nuclear fallbacks (still go hard)
        return random.choice([
            f"cinematic masterpiece of a glowing {ticker} logo made of pure diamond and molten gold rising from a sea of burning cash, thousands of apes in lambos cheering, federal reserve exploding in background, laser beams, money printer brrr, cyberpunk city at night, dramatic god rays, 8k octane render beeple style",
            f"hyper-detailed portrait of a sigma wolf wearing {ticker} chain, diamond teeth, laser eyes, standing on pile of dead bears, wall street in flames behind him, money raining, ultra realistic cinematic lighting, in the style of greg rutkowski and xcopy"
        ])