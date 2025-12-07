# app.py — CLEAN IMAGE + REEL BOT (Dec 2025) — NO MOCHI, NO DRAMA
import os
import random
from datetime import datetime
import schedule
import time

from utils.promptgen import generate_art_prompt
from utils.flux_local import generate_flux_image
from utils.instagram import post_to_instagram
from utils.twitter import post_to_x
from utils.news_fetch import get_top_headlines


def job():
    print(f"\n{'=' * 60}")
    print(f"IMAGE CYCLE STARTED — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 60}")

    # 1. Get live market inspiration
    headlines = get_top_headlines(num=3)
    selected_headline = random.choice(headlines)
    print(f"News inspiration → {selected_headline}")

    # 2. Generate modern art prompt
    prompt = generate_art_prompt(selected_headline)
    print(f"Art prompt → {prompt[:140]}...")

    # 3. Generate Flux image
    image_path = generate_flux_image(prompt)
    if not image_path:
        print("Flux generation failed — skipping this cycle")
        return

    # 4. INFINITELY FRESH GALLERY TITLES — 2025 EXPANDED EDITION
    prefixes = [
        "Volatility’s", "Liquidity’s", "The Market’s", "Gamma’s", "Regime’s",
        "Distribution’s", "Accumulation’s", "Conviction’s", "The Tape’s",
        "Fear’s", "Greed’s", "Edge’s", "The Float’s", "Institutional", "Retail",
        "Circuitry’s", "Fiscal", "Monetary", "Algorithmic", "Structural",
        "Capitulation’s", "Euphoria’s", "The Bid’s", "The Offer’s", "Delta’s",
        "Vanna’s", "Charm’s", "Theta’s", "Rho’s", "Skew’s", "Kurtosis’",
        "Dispersion’s", "Correlation’s", "Contagion’s", "Redemption’s", "Rotation’s",
        "Mean Reversion’s", "Momentum’s", "Carry’s", "Reflation’s", "Stagflation’s",
        "The Fed’s", "The ECB’s", "The BOJ’s", "Yield’s", "Spread’s"
    ]

    nouns = [
        "Veil", "Horizon", "Echo", "Fracture", "Ascent", "Descent", "Silence",
        "Crescendo", "Palimpsest", "Ledger", "Canvas", "Throne", "Cathedral",
        "Requiem", "Symphony", "Geometry", "Negative Space", "Crimson Dream",
        "Amber Moment", "Ultramarine Shift", "Obsidian Flow", "Golden Ratio",
        "Terminal Glow", "Data Cathedral", "Order-Book Halo", "Gamma Garden",
        "Volatility Smile", "Risk Premia", "Liquidity Trap", "Black-Scholes Veil",
        "Event Horizon", "Singularity", "Entropic Collapse", "Phase Transition",
        "Paradigm Drift", "Narrative Fracture", "Alpha Decay", "Omega Point",
        "Zero-Day Expiry", "Pin Risk", "Convexity Void", "Carry Graveyard",
        "Dispersion Trade", "Correlation Collapse", "Tail Hedron", "Dragon King",
        "Minsky Moment", "Hindenburg Omen", "Death Cross", "Golden Cross"
    ]

    connectors = [
        "in", "of", "as", "over", "beneath", "beyond", "within", "against",
        "through", "after", "before", "during", "under", "above", "between",
        "across", "behind", "inside", "outside", "toward", "away from",
        "at the edge of", "at the end of", "in the wake of", "on the eve of"
    ]

    structures = [
        lambda: f"{random.choice(prefixes)} {random.choice(nouns)}",
        lambda: f"{random.choice(nouns)} of {random.choice(prefixes)}",
        lambda: f"{random.choice(connectors).capitalize()} {random.choice(prefixes)} {random.choice(nouns)}",
        lambda: f"The {random.choice(nouns)} {random.choice(connectors)} {selected_headline.split(':')[0]}",
        lambda: f"{selected_headline.split(':')[0]} — {random.choice(prefixes)} {random.choice(nouns)}",
        lambda: f"{random.choice(prefixes)} {random.choice(nouns)} in the Age of {selected_headline.split()[0]}",
        lambda: f"{random.choice(nouns)} {random.choice(connectors)} {random.choice(prefixes)} Capital",
        lambda: f"After {selected_headline.split()[0]}: {random.choice(prefixes)} {random.choice(nouns)}",
        lambda: f"{random.choice(prefixes)} {random.choice(nouns)} / {random.choice(nouns)}"
    ]

    title = random.choice(structures)()

    if random.random() < 0.09:
        rare = random.choice([
            "Memento Gamma", "Post Tenebras Lux", "In Volatilitate Veritas",
            "Ars Mercatus", "Pax Volatilis", "Requiem pro Bullā", "Fiat Lux et Fiat Chart",
            "Omega Squeeze", "Alpha in Tenebris", "Ex Nihilo Pump", "Veni Vidi Vol",
            "Alea Jacta Chart", "Gamma Ex Machina", "Deus Ex Pin Risk", "Memento Minsky",
            "Hic Sunt Dracones", "Noli Tangere Circulum", "Fat Tail Fati", "Skew Semper Tyrannis",
            "Convexitas Maxima", "Theta Gang Delenda Est", "Dispersion Victrix"
        ])
        title = rare

    caption = f"\n{selected_headline}\n— {title} —\n"

    # 5. Post image + 5-second Reel
    post_to_x(image_path, caption)
    post_to_instagram(caption=caption, image_path=image_path)

    print("Daily masterpiece posted — X + IG Feed + Story + Reel\n")


# ————————————————————————
job()  # Run once immediately
schedule.every(67).minutes.do(job)

print("Financial Art Bot LIVE — Images + Reels every 67 minutes")
while True:
    schedule.run_pending()
    time.sleep(10)