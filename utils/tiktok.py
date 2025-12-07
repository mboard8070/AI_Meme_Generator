# utils/tiktok.py — Dedicated TikTok uploader (Dec 2025)
from tiktok_uploader.upload import upload_video
import os

def post_to_tiktok(video_path: str, caption: str) -> bool:
    cookies = "tiktok_cookies.txt"
    if not os.path.exists(cookies):
        print("TikTok skipped — tiktok_cookies.txt missing")
        return False
    if not os.path.exists(video_path):
        return False

    tt_caption = f"{caption[:140]} #FYP #AIArt #FinancialArt #Cinema"
    try:
        upload_video(video=video_path, description=tt_caption, cookies=cookies)
        print("TikTok posted (FYP ready)")
        return True
    except Exception as e:
        print(f"TikTok upload failed: {e}")
        return False