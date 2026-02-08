"""
Central configuration for the Telegram Trade Analyzer.
Copy .env.example to .env and fill in your values.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Project paths ──────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MESSAGES_DIR = DATA_DIR / "messages"
IMAGES_DIR = DATA_DIR / "images"
OUTPUT_DIR = DATA_DIR / "output"

# Ensure directories exist
for d in [MESSAGES_DIR, IMAGES_DIR, OUTPUT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ── Telegram credentials ──────────────────────────────────────
# Get these from https://my.telegram.org
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID", "")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "")
TELEGRAM_PHONE = os.getenv("TELEGRAM_PHONE", "")

# Channel to scrape (without https://t.me/)
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "ranjitoptions")

# ── Scraper settings ──────────────────────────────────────────
# Max messages to scrape (set to 0 for all)
MAX_MESSAGES = int(os.getenv("MAX_MESSAGES", "0"))

# Batch size for downloading
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "100"))

# ── OCR settings ─────────────────────────────────────────────
# Free API key from https://ocr.space/ocrapi/freekey
OCR_API_KEY = os.getenv("OCR_API_KEY", "")

# ── Trade parsing settings ────────────────────────────────────
# Common stock/option symbols to look for (add more as needed)
KNOWN_SYMBOLS = [
    "NIFTY", "BANKNIFTY", "FINNIFTY", "SENSEX",
    "NIFTY50", "BNF", "NF",
]

# Trade keywords
BUY_KEYWORDS = ["buy", "bought", "long", "entry", "call buy", "put buy", "ce buy", "pe buy"]
SELL_KEYWORDS = ["sell", "sold", "short", "exit", "book profit", "booked", "sl hit", "target hit"]
