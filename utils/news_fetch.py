# utils/news_fetch.py — Live financial headlines for art-inspired captions
import requests
from xml.etree import ElementTree as ET
import random

def get_top_headlines(num=3):
    try:
        # Yahoo Finance RSS — free, updated hourly
        rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline"
        response = requests.get(rss_url, timeout=10)
        root = ET.fromstring(response.content)
        headlines = [item.find('title').text for item in root.findall('.//item') if item.find('title') is not None][:num]
        return headlines if headlines else ["Markets in quiet ascent."]
    except:
        # Fallbacks based on today's meta (rate cuts, AI capex, Black Friday)
        return random.choice([
            ["Intel's Surge: Circuits of Ambition", "Nvidia's Shadow: The Pullback Palette", "Gold at $4,220: Fiscal Flight"],
            ["Meta's AI Bill: Capex Canvas", "Rate Cut Hopes: Volatility's Veil", "Black Friday Rally: Consumer Echoes"],
            ["Nasdaq Snaps Streak: Technical Twilight", "Goldman on Gold: Institutional Ink", "Jefferies Probe: Regulatory Red"]
        ])