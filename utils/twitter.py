# utils/twitter.py — posts images + text to X (Twitter) flawlessly
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # reads your .env (same as main bot)

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

auth = tweepy.OAuth1UserHandler(
    os.getenv("API_KEY"),
    os.getenv("API_KEY_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)
api_v1 = tweepy.API(auth)


def post_to_x(image_path: str, text: str):
    if not os.path.exists(image_path):
        print("X post skipped — image missing")
        return False

    try:
        media = api_v1.media_upload(filename=image_path)
        client.create_tweet(text=text, media_ids=[media.media_id])
        print(f"[{__import__('datetime').datetime.now().strftime('%H:%M')}] X post SUCCESS")
        return True
    except Exception as e:
        print(f"X post failed: {e}")
        return False