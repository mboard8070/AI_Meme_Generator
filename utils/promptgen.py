# utils/promptgen.py — Modern Financial Art Prompts (2025)
import random

def generate_art_prompt(news_headline: str) -> str:
    """
    Generates a single, highly detailed Flux prompt inspired by current news,
    styled like a contemporary art piece.
    """
    styles = [
        "in the style of Gerhard Richter and Jenny Saville, oil on canvas, dramatic lighting",
        "abstract expressionist masterpiece, Rothko meets Basquiat, textured impasto",
        "digital surrealism, Refik Anadol data painting, volumetric light beams",
        "glitch art meets renaissance portrait, Caravaggio lighting, 8k detail",
        "neon noir cyberpunk, Blade Runner aesthetics, cinematic composition",
        "minimalist brutalism with financial symbols, Bauhaus meets Bloomberg terminal",
        "hyperrealist financial surrealism, Gregory Crewdson meets trading floor",
        "in the style of Agnes Martin and financial data visualization, subtle grid systems"
    ]

    moods = [
        "melancholic reflection on market cycles",
        "euphoric ascent amid volatility",
        "quiet tension before the breakout",
        "institutional calm masking retail panic",
        "algorithmic serenity in chaos",
        "the weight of conviction in negative space",
        "distribution disguised as accumulation",
        "the silence after the gamma squeeze"
    ]

    elements = [
        "floating ticker symbols made of light",
        "shattered candlestick charts in mid-air",
        "a lone wolf made of circuit traces and gold",
        "bear silhouettes dissolving into data streams",
        "hands reaching for falling liquidity",
        "eyes made of order books, reflecting fear and greed",
        "a throne built from failed IPOs",
        "volatility surface rendered as stained glass"
    ]

    prompt = f"""
    A contemporary financial artwork inspired by the headline "{news_headline}",
    {random.choice(styles)},
    {random.choice(moods)},
    featuring {random.choice(elements)},
    museum-quality, gallery lighting, award-winning composition,
    ultra detailed, emotionally charged, 8k, masterpiece
    """.strip().replace("\n", " ").strip()

    return prompt