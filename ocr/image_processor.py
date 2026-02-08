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
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from tqdm import tqdm

import config

# Free API endpoint
OCR_API_URL = "https://api.ocr.space/parse/image"


def preprocess_image(image_path: str) -> bytes:
    """
    Preprocess trade screenshot for maximum OCR accuracy.
    - Upscale small images to 2000px+ width
    - Convert to high-contrast grayscale
    - Sharpen text edges
    - Auto-adjust brightness/contrast
    - Save as high-quality PNG (better for OCR than JPEG)
    """
    img = Image.open(image_path)

    # Convert to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Step 1: Upscale aggressively — OCR needs big, clear text
    target_width = 2000
    if img.width < target_width:
        ratio = target_width / img.width
        new_w = int(img.width * ratio)
        new_h = int(img.height * ratio)
        img = img.resize((new_w, new_h), Image.LANCZOS)

    # Step 2: Auto-contrast (normalizes brightness across the image)
    img = ImageOps.autocontrast(img, cutoff=1)

    # Step 3: Increase sharpness (makes text edges crisp)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)

    # Step 4: Boost contrast (makes text stand out from background)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.8)

    # Step 5: Slight brightness boost (trade screenshots are often dark)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2)

    # Convert to PNG bytes (lossless, better for OCR than JPEG)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    img_bytes = buf.getvalue()

    # If PNG is over 1MB (API limit), fall back to high-quality JPEG
    if len(img_bytes) > 1024 * 1024:
        # Reduce size slightly
        max_width = 1600
        if img.width > max_width:
            ratio = max_width / img.width
            img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=95)
        buf.seek(0)
        img_bytes = buf.getvalue()

    return img_bytes


def ocr_with_api(image_path: str, api_key: str) -> str:
    """
    Extract text from image using free ocr.space API.
    Tries Engine 2 first (better for screenshots), falls back to Engine 1.
    """
    img_bytes = preprocess_image(image_path)
    file_ext = "png" if img_bytes[:4] == b'\x89PNG' else "jpg"
    mime = "image/png" if file_ext == "png" else "image/jpeg"

    # Try Engine 2 first (better for screenshots and complex layouts)
    text = _call_api(img_bytes, api_key, engine="2", mime=mime, ext=file_ext)

    # If Engine 2 got very little text, try Engine 1 as fallback
    if len(text.strip()) < 10:
        text2 = _call_api(img_bytes, api_key, engine="1", mime=mime, ext=file_ext)
        if len(text2.strip()) > len(text.strip()):
            text = text2

    return text.strip()


def _call_api(img_bytes: bytes, api_key: str, engine: str, mime: str, ext: str) -> str:
    """Make a single OCR API call."""
    resp = requests.post(
        OCR_API_URL,
        files={"file": (f"image.{ext}", img_bytes, mime)},
        data={
            "apikey": api_key,
            "language": "eng",
            "isOverlayRequired": False,
            "OCREngine": engine,
            "scale": True,           # Let API also upscale
            "isTable": True,         # Better for tabular trade data
            "detectOrientation": True,
        },
        timeout=60,
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

    return parsed[0].get("ParsedText", "")


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

    def process_all_images(self, messages: list = None, fresh: bool = False) -> list:
        """
        Process all images via OCR API.
        Set fresh=True to delete old results and start over.
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
        print(f"  Preprocessing: upscale to 2000px, auto-contrast, sharpen, boost")
        print(f"  OCR: Engine 2 (screenshots) with Engine 1 fallback")

        # Fresh start: delete old results
        if fresh and self.results_file.exists():
            self.results_file.unlink()
            print("  Deleted old OCR results — starting fresh")

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

            # Rate limit: ~1.5 seconds between calls to stay safe
            # Using both engines doubles API calls, so slightly longer wait
            time.sleep(2)

        self._save_results(results)
        good = sum(1 for r in results if r.get("ocr_text"))
        print(f"\nDone! Processed {len(results)} images")
        print(f"  Text extracted: {good} | Empty/errors: {len(results) - good}")
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
