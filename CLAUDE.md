# CLAUDE.md

> Reference guide for AI assistants working in this repository.

## Repository Overview

- **Name:** ppt (Telegram Trade Analyzer)
- **Owner:** jitendrajainnew
- **Purpose:** Scrape messages and images from a Telegram trading channel, extract trade data via OCR, parse structured trade info, and analyze trading performance. Tuned for the Indian options market (NIFTY, BANKNIFTY, CE/PE instruments).

## Project Structure

```
ppt/
├── CLAUDE.md                    # AI assistant guide (this file)
├── main.py                      # Main CLI orchestrator (entry point)
├── config.py                    # Central configuration (reads from .env)
├── requirements.txt             # Python dependencies
├── .env.example                 # Template for environment variables
├── .gitignore
├── scraper/
│   ├── __init__.py
│   └── telegram_scraper.py      # Telegram API + web fallback scraper
├── ocr/
│   ├── __init__.py
│   └── image_processor.py       # OCR via ocr.space API
├── parser/
│   ├── __init__.py
│   └── trade_parser.py          # Regex-based trade data extractor
├── analysis/
│   ├── __init__.py
│   └── analyzer.py              # Statistics, charts, Excel reports
├── scripts/
│   └── .gitkeep
└── data/                        # Runtime data (git-ignored contents)
    ├── messages/                 # Scraped messages JSON
    ├── images/                   # Downloaded trade images
    └── output/                   # Parsed trades, reports, charts
```

## Getting Started

```bash
# 1. Create virtual environment
python -m venv venv && source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure credentials
cp .env.example .env
# Edit .env — see "Environment Variables" section below

# 4. Run (web scraper needs no Telegram credentials)
python main.py all --web
```

## Common Commands

```bash
python main.py scrape          # Scrape via Telethon API (needs credentials)
python main.py scrape --web    # Scrape via public web preview (no credentials)
python main.py ocr             # Run OCR on downloaded images
python main.py parse           # Parse trade data from text + OCR
python main.py analyze         # Generate stats, Excel report, charts
python main.py all             # Run full pipeline (API scraper)
python main.py all --web       # Full pipeline with web scraper
```

## Architecture

### Pipeline Overview

The pipeline has 4 sequential stages orchestrated by `main.py`:

```
Scrape → OCR → Parse → Analyze
```

1. **Scrape** (`scraper/telegram_scraper.py`) — Downloads messages and images from the Telegram channel. Two modes:
   - `TelegramScraper`: Uses Telethon API (full access, requires API credentials and phone number)
   - `WebScraper`: Parses public channel web preview at `t.me/s/{channel}` via BeautifulSoup (no credentials needed)
   - Output: `data/messages/messages.json`

2. **OCR** (`ocr/image_processor.py`) — Extracts text from trade screenshot images using the **ocr.space API** (free tier, requires API key). Includes image preprocessing (resize, contrast enhancement, sharpening via Pillow). Supports resume (skips already-processed images).
   - Input: `data/messages/messages.json` (reads `image_path` fields)
   - Output: `data/output/ocr_results.json`

3. **Parse** (`parser/trade_parser.py`) — Uses regex patterns to extract structured trade fields (symbol, strike, entry/exit price, SL, target, instrument type, etc.) from message text and OCR text. Merges data from both sources with confidence scoring.
   - Input: `data/messages/messages.json` + `data/output/ocr_results.json`
   - Output: `data/output/trades.json`

4. **Analyze** (`analysis/analyzer.py`) — Computes statistics (win rate, P&L, risk-reward, streaks, time-of-day analysis), generates an Excel report with multiple sheets, and produces matplotlib chart PNGs.
   - Input: `data/output/trades.json`
   - Output: `data/output/trade_stats.json`, `data/output/trade_report.xlsx`, `data/output/charts/*.png`

### Data Flow

```
data/messages/messages.json        ← Scraper output
    ↓
data/output/ocr_results.json       ← OCR output (reads image_path from messages)
    ↓
data/output/trades.json            ← Parser output (merges messages + OCR)
    ↓
data/output/trade_stats.json       ← Analyzer: statistics
data/output/trade_report.xlsx      ← Analyzer: Excel report (5 sheets)
data/output/charts/*.png           ← Analyzer: 6 visualization charts
```

## Key Classes and Functions

### `scraper/telegram_scraper.py`

| Class/Function | Purpose |
|---|---|
| `TelegramScraper` | Telethon-based async scraper. Methods: `connect()`, `scrape_channel()`, `_save_messages()` |
| `WebScraper` | BeautifulSoup-based sync scraper for public channels. Methods: `scrape_channel()`, `_save_messages()` |
| `run_api_scraper()` | Async wrapper to run `TelegramScraper` |
| `run_web_scraper()` | Sync wrapper to run `WebScraper` |

### `ocr/image_processor.py`

| Class/Function | Purpose |
|---|---|
| `preprocess_image(path)` | Resizes (max 1200px width), enhances contrast (1.3x), sharpens, returns JPEG bytes |
| `ocr_with_api(path, key)` | Posts image to `https://api.ocr.space/parse/image` (OCREngine=2), returns extracted text |
| `ImageProcessor` | Batch processor. Methods: `process_all_images()`, `_load_existing_results()`, `_save_results()` |

### `parser/trade_parser.py`

| Class/Function | Purpose |
|---|---|
| `Trade` (dataclass) | 16-field structured trade record (symbol, instrument, prices, P&L, confidence, etc.) |
| `TradeParser` | Regex-based parser. Methods: `parse_all()`, `_parse_text()`, `_merge_trades()`, `_save_trades()` |

### `analysis/analyzer.py`

| Class/Function | Purpose |
|---|---|
| `TradeAnalyzer` | Full analysis engine. Methods: `load_trades()`, `compute_stats()`, `generate_excel_report()`, `generate_charts()`, `print_summary()` |
| `_max_streak(values, target)` | Static helper: calculates max consecutive occurrences |

## Environment Variables

Configured via `.env` file (see `.env.example`):

| Variable | Required | Default | Description |
|---|---|---|---|
| `TELEGRAM_API_ID` | For API scraper | `""` | Integer from https://my.telegram.org |
| `TELEGRAM_API_HASH` | For API scraper | `""` | String from https://my.telegram.org |
| `TELEGRAM_PHONE` | For API scraper | `""` | Phone with country code (e.g., `+91xxxxxxxxxx`) |
| `TELEGRAM_CHANNEL` | No | `"ranjitoptions"` | Channel username to scrape |
| `MAX_MESSAGES` | No | `0` (all) | Limit number of messages scraped |
| `BATCH_SIZE` | No | `100` | Save progress every N messages |
| `OCR_API_KEY` | For OCR stage | `""` | Free key from https://ocr.space/ocrapi/freekey |

## Dependencies

From `requirements.txt` (Python 3.8+):

| Package | Min Version | Purpose |
|---|---|---|
| `telethon` | 1.34.0 | Telegram API client |
| `aiohttp` | 3.9.0 | Async HTTP (Telethon dependency) |
| `Pillow` | 10.0.0 | Image preprocessing |
| `pandas` | 2.1.0 | Data analysis and DataFrames |
| `openpyxl` | 3.1.0 | Excel file generation |
| `matplotlib` | 3.8.0 | Chart visualization |
| `tqdm` | 4.66.0 | Progress bars |
| `python-dotenv` | 1.0.0 | `.env` file loading |
| `beautifulsoup4` | 4.12.0 | HTML parsing (web scraper) |
| `requests` | 2.31.0 | HTTP requests (web scraper + OCR API) |

## Code Conventions

- **Language:** Python 3.8+ (uses f-strings, dataclasses, pathlib, asyncio)
- **Naming:** `snake_case` for functions/variables, `PascalCase` for classes
- **Config:** All settings centralized in `config.py`, loaded from `.env` via `python-dotenv`
- **Paths:** Uses `pathlib.Path` objects, not raw strings
- **Data storage:** JSON files with `indent=2`, `ensure_ascii=False`, UTF-8 encoding
- **Error handling:** Print-based messages with `sys.exit(1)` for fatal errors; no logging framework
- **Progress:** `tqdm` progress bars for batch operations; formatted console output with `"=" * 50` separators
- **Async:** Used only in `TelegramScraper` (Telethon requires it); everything else is synchronous
- **Type hints:** Minimal; present in `Trade` dataclass fields but not widely used elsewhere
- **Tests:** No test framework or test files currently exist
- **CI/CD:** No CI/CD configuration currently exists

## Key Configuration Constants (in `config.py`)

- **`KNOWN_SYMBOLS`** — List of 65+ recognized stock/option symbols (NIFTY, BANKNIFTY, FINNIFTY, RELIANCE, TCS, HDFCBANK, etc.). Extend this list to recognize additional symbols.
- **`BUY_KEYWORDS`** — `["buy", "bought", "long", "entry", "call buy", "put buy", "ce buy", "pe buy"]`
- **`SELL_KEYWORDS`** — `["sell", "sold", "short", "exit", "book profit", "booked", "sl hit", "target hit"]`

## Trade Parser Details

The parser in `parser/trade_parser.py` is the most complex module and the key area for tuning accuracy.

**Regex patterns** extract:
- Symbol + strike + instrument (e.g., "NIFTY 23400 CE")
- Entry, target, stop-loss, and exit prices
- Expiry dates (e.g., "21 Feb")
- Quantity/lots
- Trade type (BUY/SELL) from keyword matching

**Confidence scoring** (0.0–1.0):
- Trade type detected: +0.2 to +0.3
- Symbol + strike extracted: +0.4
- Each price field extracted: +0.05 to +0.1
- Trades below 0.1 confidence are discarded

**Trade status** is auto-determined: `OPEN`, `CLOSED`, `TARGET_HIT`, `SL_HIT`

**P&L calculation**: `exit_price - entry_price` for BUY trades, `entry_price - exit_price` for SELL trades

## Analyzer Outputs

### Excel Report (`trade_report.xlsx`) — 5 sheets:
1. **All Trades** — Full trade data
2. **Summary** — Key metrics (total trades, P&L stats, win rate, risk-reward)
3. **By Symbol** — Top symbols by trade count
4. **By Month** — Monthly trade counts
5. **Monthly P&L** — Monthly P&L aggregation with win rates

### Charts (`data/output/charts/`) — 6 PNG files:
1. `cumulative_pnl.png` — Line chart of cumulative P&L over time
2. `win_rate.png` — Pie chart (winners vs losers)
3. `pnl_distribution.png` — Histogram of P&L values
4. `by_symbol.png` — Horizontal bar chart of top 10 symbols
5. `by_hour.png` — Bar chart of trades by hour of day
6. `monthly_pnl.png` — Color-coded monthly P&L bars (green=profit, red=loss)

## Notes for AI Assistants

- Always read this file at the start of a session to understand current project state
- The `data/` directory contents are git-ignored; all runtime data lives there
- **Never commit** `.env` or `*.session` / `*.session-journal` files (contain credentials)
- The trade parser regex patterns in `parser/trade_parser.py` are the key area for tuning accuracy
- `config.py` has `KNOWN_SYMBOLS`, `BUY_KEYWORDS`, `SELL_KEYWORDS` lists that can be extended to support new symbols/phrases
- OCR uses the **ocr.space API** (not local Tesseract/EasyOCR) — requires a free API key and has rate limits (~500 calls/day, 1.5s between calls)
- OCR results support resume — rerunning skips already-processed images (saves progress every 25 images)
- The web scraper (`--web` flag) works without any credentials on public channels; the API scraper needs Telegram credentials
- Update this file when significant structural changes are made
