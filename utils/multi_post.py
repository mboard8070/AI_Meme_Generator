# utils/multi_post.py — Tiny coordinator — keeps everything separate
from utils.instagram import post_to_instagram
from utils.youtube import post_to_youtube
from utils.tiktok import post_to_tiktok
import os
import time
from datetime import datetime

def post_everywhere(video_path: str, caption: str):
    if not os.path.exists(video_path):
        print("Multi-post aborted — video missing")
        return

    results = {
        "Instagram": post_to_instagram(caption=caption, image_path=video_path),  # your perfect IG script
        "YouTube":   post_to_youtube(video_path, caption),
        "TikTok":    post_to_tiktok(video_path, caption)
    }

    success = sum(results.values())
    print(f"[{datetime.now().strftime('%H:%M:%S')}] MULTI-POST: {success}/3 platforms live")

    # Safe cleanup
    for _ in range(10):
        try:
            os.unlink(video_path)
            break
        except PermissionError:
            time.sleep(1)