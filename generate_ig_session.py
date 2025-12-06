# generate_ig_session.py — run this ONCE to create a mobile session
from instagrapi import Client
import os
from dotenv import load_dotenv
load_dotenv()

cl = Client()
cl.delay_range = [1, 5]

# Use your .env creds (fallback to sessionid if no password)
username = os.getenv("INSTA_USER") or input("IG Username: ")
password = os.getenv("INSTA_PASS") or input("IG Password: ")
sessionid = os.getenv("INSTA_SESSIONID")

if password:
    cl.login(username, password)
elif sessionid:
    cl.login_by_sessionid(sessionid)
else:
    print("Need username/password or sessionid in .env")
    exit(1)

# Save the FULL mobile session (way more reliable than just sessionid)
cl.dump_settings("ig_session.json")
print("✅ Mobile session saved to ig_session.json")
print("Copy this file to your bot folder and update instagram.py")