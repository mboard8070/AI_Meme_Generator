# generate_ig_session.py — FINAL WORKING VERSION (NO ERRORS)
from instagrapi import Client
from instagrapi.exceptions import *
import os
from dotenv import load_dotenv
import time

load_dotenv()

cl = Client()
cl.delay_range = [5, 12]  # safe for home IP

username = os.getenv("INSTA_USER") or input("Instagram username: ")
password = os.getenv("INSTA_PASS") or input("Instagram password: ")

print(f"\nLogging in as @{username}...")

try:
    cl.login(username, password)
    print("Logged in successfully!")
except BadPassword:
    print("Wrong password or 2FA is on. Try again or disable 2FA temporarily.")
    exit()
except ChallengeRequired:
    print("Instagram sent a security code (check email/SMS/app)")
    code = input("Enter the 6-digit code: ")
    try:
        cl.challenge_resolve(code)
        print("Challenge solved!")
    except:
        print("Wrong/expired code.")
        exit()
except PleaseWaitFewMinutes:
    print("Instagram says wait a few minutes. Wait 10–15 min and try again.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

# Save session
cl.dump_settings("ig_session.json")
print("\nSUCCESS! ig_session.json created")
print("Copy this file into both your trading-bot and meme-bot folders.")