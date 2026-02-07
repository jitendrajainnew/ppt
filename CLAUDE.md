# CLAUDE.md

> Reference guide for AI assistants working in this repository.

## Repository Overview

- **Name:** ppt (Telegram Trade Analyzer)
- **Owner:** jitendrajainnew
- **Purpose:** Scrape messages and images from a Telegram trading channel, extract trade data via OCR, parse structured trade info, and analyze trading performance.

## Project Structure

```
ppt/
├── CLAUDE.md               # AI assistant guide (this file)
├── main.py                 # Main orchestrator (CLI entry point)
├── config.py               # Central configuration (reads from .env)
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── .gitignore
├── scraper/
│   └── telegram_scraper.py # Telegram API + web fallback scraper
├── ocr/
│   └── image_processor.py  # OCR pipeline (Tesseract / EasyOCR)
├── parser/
│   └── trade_parser.py     # Regex-based trade data extractor
├── analysis/
│   └── analyzer.py         # Statistics, charts, Excel reports
└── data/                   # Runtime data (git-ignored)
    ├── messages/            # Scraped messages JSON
    ├── images/              # Downloaded trade images
    └── output/              # Parsed trades, reports, charts
```

## Getting Started

```bash
# 1. Create virtual environment
python -m venv venv && source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure credentials
cp .env.example .env
# Edit .env with your Telegram API ID/Hash from https://my.telegram.org

# 4. Run (web scraper needs no credentials)
python main.py all --web
```

## Common Commands

```bash
python main.py scrape          # Scrape via Telethon API
python main.py scrape --web    # Scrape via public web preview
python main.py ocr             # Run OCR on downloaded images
python main.py parse           # Parse trade data from text + OCR
python main.py analyze         # Generate stats, Excel report, charts
python main.py all             # Run full pipeline
python main.py all --web       # Full pipeline with web scraper
```

## Architecture

The pipeline has 4 sequential stages:

1. **Scrape** (`scraper/telegram_scraper.py`) — Downloads messages + images from the Telegram channel. Two modes: Telethon API (full access, needs credentials) and web scraper (public channels only, no credentials).
2. **OCR** (`ocr/image_processor.py`) — Extracts text from trade screenshot images. Supports Tesseract and EasyOCR. Includes image preprocessing (grayscale, contrast, sharpen). Supports resume.
3. **Parse** (`parser/trade_parser.py`) — Uses regex patterns to extract structured trade fields (symbol, strike, entry/exit price, SL, target, instrument type, etc.) from message text and OCR text. Merges data from both sources.
4. **Analyze** (`analysis/analyzer.py`) — Computes stats (win rate, P&L, risk-reward, streaks, time analysis), generates Excel report with multiple sheets, and produces matplotlib charts.

Data flows as JSON between stages: `messages.json` → `ocr_results.json` → `trades.json` → reports.

## Code Conventions

- **Language:** Python 3.8+
- **Config:** All settings in `config.py`, loaded from `.env` via `python-dotenv`
- **Data storage:** JSON files in `data/` directory (git-ignored)
- **OCR engines:** Configurable via `OCR_ENGINE` env var (`easyocr` or `tesseract`)
- **Trade parsing:** Regex-based, tuned for Indian options market (NIFTY, BANKNIFTY, CE/PE)

## Notes for AI Assistants

- Always read this file at the start of a session to understand current project state
- The `data/` directory is git-ignored; all runtime data lives there
- Never commit `.env` or `*.session` files (contain credentials)
- The trade parser regex patterns in `parser/trade_parser.py` are the key area for tuning accuracy
- `config.py` has `KNOWN_SYMBOLS`, `BUY_KEYWORDS`, `SELL_KEYWORDS` lists that can be extended
- OCR results support resume — rerunning skips already-processed images
- Update this file when significant structural changes are made
