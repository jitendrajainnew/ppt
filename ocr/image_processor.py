"""
OCR pipeline for extracting text from trade screenshot images.
Uses free ocr.space API — no local OCR libraries needed.
Just needs requests + Pillow (already installed).

Get your free API key at: https://ocr.space/ocrapi/freekey
Free tier: 25,000 requests/month (plenty for 6000 images).
"""

import io
import json
import time
from pathlib import Path

import requests
from PIL import Image, ImageEnhance, ImageFilter
from tqdm import tqdm

import config

# Free API endpoint
OCR_API_URL = "https://api.ocr.space/parse/image"


def preprocess_image(image_path: str) -> bytes:
    """
    Preprocess image and return as JPEG bytes (under 1MB for free API).
    """
    img = Image.open(image_path)

    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    if img.mode == "L":
        img = img.convert("RGB")

    # Resize if too large (free API limit is 1MB)
    max_width = 1200
    if img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.3)

    # Sharpen
    img = img.filter(ImageFilter.SHARPEN)

    # Convert to JPEG bytes
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    buf.seek(0)
    return buf.getvalue()


def ocr_with_api(image_path: str, api_key: str) -> str:
    """Extract text from image using free ocr.space API."""
    img_bytes = preprocess_image(image_path)

    resp = requests.post(
        OCR_API_URL,
        files={"file": ("image.jpg", img_bytes, "image/jpeg")},
        data={
            "apikey": api_key,
            "language": "eng",
            "isOverlayRequired": False,
            "OCREngine": "2",  # Engine 2 is better for screenshots
        },
        timeout=30,
    )

    if resp.status_code != 200:
        raise Exception(f"API returned HTTP {resp.status_code}")

    result = resp.json()

    if result.get("IsErroredOnProcessing"):
        error_msg = result.get("ErrorMessage", ["Unknown error"])
        raise Exception(f"OCR API error: {error_msg}")

    parsed = result.get("ParsedResults", [])
    if not parsed:
        return ""

    text = parsed[0].get("ParsedText", "")
    return text.strip()


class ImageProcessor:
    """Batch OCR processor using free ocr.space API."""

    def __init__(self):
        self.api_key = config.OCR_API_KEY
        self.results_file = config.OUTPUT_DIR / "ocr_results.json"

        if not self.api_key:
            print("=" * 55)
            print("  OCR API KEY NEEDED (free, takes 30 seconds)")
            print("=" * 55)
            print()
            print("  1. Go to: https://ocr.space/ocrapi/freekey")
            print("  2. Enter your email")
            print("  3. Copy the API key from the email")
            print("  4. Add to your .env file:")
            print("     OCR_API_KEY=your_key_here")
            print()
            print("  Free tier: 25,000 requests/month")
            print("=" * 55)
            raise SystemExit(1)

    def process_all_images(self, messages: list = None) -> list:
        """
        Process all images via OCR API.
        Supports resume — rerunning skips already-processed images.
        """
        if messages is None:
            messages_file = config.MESSAGES_DIR / "messages.json"
            if not messages_file.exists():
                print("ERROR: No messages.json found. Run the scraper first.")
                return []
            with open(messages_file, "r") as f:
                messages = json.load(f)

        # Filter messages with images
        image_tasks = []
        for msg in messages:
            if msg.get("image_path") and Path(msg["image_path"]).exists():
                image_tasks.append((msg["image_path"], msg["id"]))

        if not image_tasks:
            print("No images found to process.")
            return []

        print(f"Processing {len(image_tasks)} images via ocr.space API...")

        # Load existing results to support resume
        existing_results = self._load_existing_results()
        processed_ids = {r["msg_id"] for r in existing_results}

        remaining = [t for t in image_tasks if t[1] not in processed_ids]
        if len(image_tasks) - len(remaining) > 0:
            print(f"  Skipping {len(image_tasks) - len(remaining)} already processed images")
        if not remaining:
            print("  All images already processed!")
            return existing_results

        print(f"  {len(remaining)} images to process")

        results = list(existing_results)
        errors = 0

        for image_path, msg_id in tqdm(remaining, desc="OCR"):
            try:
                text = ocr_with_api(image_path, self.api_key)
                results.append({
                    "msg_id": msg_id,
                    "image_path": image_path,
                    "ocr_text": text,
                    "error": None,
                })
            except Exception as e:
                error_str = str(e)
                results.append({
                    "msg_id": msg_id,
                    "image_path": image_path,
                    "ocr_text": "",
                    "error": error_str,
                })
                errors += 1

                # If rate limited, wait and retry
                if "rate" in error_str.lower() or "limit" in error_str.lower():
                    print(f"\n  Rate limited. Waiting 60 seconds...")
                    time.sleep(60)

            # Save progress every 25 images
            if len(results) % 25 == 0:
                self._save_results(results)

            # Rate limit: free tier allows ~500 calls/day
            # ~1.5 seconds between calls is safe
            time.sleep(1.5)

        self._save_results(results)
        print(f"\nDone! Processed {len(results)} images ({errors} errors)")
        print(f"Results saved to: {self.results_file}")

        return results

    def _load_existing_results(self) -> list:
        """Load existing OCR results for resume support."""
        if self.results_file.exists():
            with open(self.results_file, "r") as f:
                return json.load(f)
        return []

    def _save_results(self, results: list):
        """Save OCR results to JSON."""
        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
