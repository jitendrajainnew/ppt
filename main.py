#!/usr/bin/env python3
"""
Telegram Trade Analyzer - Main Orchestrator
============================================

Usage:
    python main.py scrape          # Step 1: Scrape Telegram channel
    python main.py scrape --web    # Step 1: Scrape via web (no API key needed)
    python main.py ocr             # Step 2: Run OCR on downloaded images
    python main.py ocr --fresh     # Step 2: Delete old results, start over
    python main.py ocr --limit 5   # Step 2: OCR only first 5 images (for testing)
    python main.py parse           # Step 3: Parse trade data from text + OCR
    python main.py analyze         # Step 4: Analyze trades and generate reports
    python main.py all             # Run all steps sequentially
    python main.py all --web       # Run all steps using web scraper
"""

import asyncio
import argparse
import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

import config


def step_scrape(use_web: bool = False):
    """Step 1: Scrape messages and images from Telegram."""
    print("\n[STEP 1] Scraping Telegram channel...")
    print(f"  Channel: {config.TELEGRAM_CHANNEL}")
    print(f"  Method:  {'Web preview' if use_web else 'Telethon API'}")
    print()

    from scraper.telegram_scraper import run_api_scraper, run_web_scraper

    if use_web:
        return run_web_scraper()
    else:
        return asyncio.run(run_api_scraper())


def step_ocr(fresh: bool = False, limit: int = 0):
    """Step 2: Run OCR on all downloaded images."""
    print("\n[STEP 2] Running OCR on images...")
    print(f"  Using: ocr.space free API (improved preprocessing)")
    if limit > 0:
        print(f"  Limit: first {limit} images only (demo mode)")
    if fresh:
        print(f"  Fresh: deleting old results, starting over")
    print()

    from ocr.image_processor import ImageProcessor
    processor = ImageProcessor()

    # If limit is set, only process first N images
    if limit > 0:
        messages_file = config.MESSAGES_DIR / "messages.json"
        if not messages_file.exists():
            print("ERROR: No messages.json found. Run the scraper first.")
            return []
        with open(messages_file, "r") as f:
            messages = json.load(f)

        # Filter only messages with images, take first N
        image_msgs = [m for m in messages if m.get("image_path") and Path(m["image_path"]).exists()]
        limited = image_msgs[:limit]
        print(f"  Selected {len(limited)} images for demo\n")

        results = processor.process_all_images(messages=limited, fresh=fresh)

        # Show OCR results for demo
        print("\n" + "=" * 60)
        print("  OCR DEMO RESULTS")
        print("=" * 60)
        for r in results:
            print(f"\n--- MSG {r['msg_id']} ---")
            print(f"Image: {r['image_path']}")
            if r["ocr_text"]:
                print(f"OCR Text:\n{r['ocr_text'][:500]}")
            else:
                print(f"Error: {r.get('error', 'No text found')}")
        print("=" * 60)

        return results
    else:
        return processor.process_all_images(fresh=fresh)


def step_parse():
    """Step 3: Parse trade data from text and OCR results."""
    print("\n[STEP 3] Parsing trade data...")
    print()

    from parser.trade_parser import TradeParser
    parser = TradeParser()
    return parser.parse_all()


def step_analyze():
    """Step 4: Analyze trades and generate reports."""
    print("\n[STEP 4] Analyzing trades...")
    print()

    from analysis.analyzer import TradeAnalyzer
    analyzer = TradeAnalyzer()
    analyzer.load_trades()
    analyzer.print_summary()
    analyzer.generate_excel_report()

    print("\nGenerating charts...")
    analyzer.generate_charts()

    return analyzer


def main():
    parser = argparse.ArgumentParser(
        description="Telegram Trade Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "step",
        choices=["scrape", "ocr", "parse", "analyze", "all"],
        help="Which step to run",
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Use web scraper instead of Telethon API (no credentials needed)",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Delete old OCR results and start over from scratch",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit OCR to first N images (for testing, e.g. --limit 5)",
    )

    args = parser.parse_args()

    print("=" * 50)
    print("  TELEGRAM TRADE ANALYZER")
    print("=" * 50)

    if args.step == "scrape":
        step_scrape(use_web=args.web)

    elif args.step == "ocr":
        step_ocr(fresh=args.fresh, limit=args.limit)

    elif args.step == "parse":
        step_parse()

    elif args.step == "analyze":
        step_analyze()

    elif args.step == "all":
        step_scrape(use_web=args.web)
        step_ocr(fresh=args.fresh, limit=args.limit)
        step_parse()
        step_analyze()

    print("\nDone!")


if __name__ == "__main__":
    main()
