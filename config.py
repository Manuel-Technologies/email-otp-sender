
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")

if not SENDER_EMAIL or not PASSWORD:
    raise ValueError("Please set the SENDER_EMAIL and PASSWORD environment variables.")
