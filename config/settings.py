from dotenv import load_dotenv
import os
load_dotenv()

# === SAME AS YOUR CHART BOT ===
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

INSTA_SESSION_FILE = "ig_session.json"     # ← CORRECT when everything is flat   # ← this is correct
POST_TO_X = True
POST_TO_INSTAGRAM = True

# Meme bot specific
POST_INTERVAL_MINUTES = 67
FLUX_STEPS = 28
IMAGE_SIZE = "1024x1024"