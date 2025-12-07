# utils/youtube.py — Dedicated YouTube Shorts uploader (Dec 2025)
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
TOKEN_FILE = "youtube_token.json"
CLIENT_SECRETS = os.getenv("YOUTUBE_CLIENT_SECRETS_PATH", "client_secrets.json")

def get_youtube_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
    return build('youtube', 'v3', credentials=creds)

def post_to_youtube(video_path: str, caption: str) -> bool:
    if not os.path.exists(video_path):
        print("YouTube skipped — video missing")
        return False

    youtube = get_youtube_service()
    title = caption.split('\n')[0][:60] + " | AI Financial Cinema"
    description = f"{caption}\n\n#Shorts #AIFilm #FinancialArt #Flux #DailyCinema"

    body = {
        "snippet": {"title": title, "description": description, "tags": ["Shorts", "AI Art", "Finance", "Flux"], "categoryId": "22"},
        "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False}
    }

    try:
        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True)
        )
        response = request.execute()
        print(f"YouTube Short posted → https://youtube.com/shorts/{response['id']}")
        return True
    except Exception as e:
        print(f"YouTube upload failed: {e}")
        return False