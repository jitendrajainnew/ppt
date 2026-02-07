"""
OCR pipeline for extracting text from trade screenshot images.
Supports both Tesseract and EasyOCR backends.
"""

import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter
from tqdm import tqdm

import config


def preprocess_image(image_path: str) -> Image.Image:
    """
    Preprocess an image for better OCR accuracy.
    - Convert to grayscale
    - Enhance contrast
    - Sharpen
    - Resize if too small
    """
    img = Image.open(image_path)

    # Convert to RGB if needed (handles RGBA, palette, etc.)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    # Convert to grayscale
    img = img.convert("L")

    # Resize small images for better OCR
    min_width = 800
    if img.width < min_width:
        ratio = min_width / img.width
        img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    # Sharpen
    img = img.filter(ImageFilter.SHARPEN)

    return img


def ocr_with_tesseract(image_path: str) -> str:
    """Extract text using Tesseract OCR."""
    import pytesseract

    img = preprocess_image(image_path)
    # Use --psm 6 for uniform block of text, --oem 3 for default LSTM engine
    custom_config = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(img, config=custom_config)
    return text.strip()


def ocr_with_easyocr(image_path: str, reader=None) -> str:
    """Extract text using EasyOCR."""
    import easyocr

    if reader is None:
        reader = easyocr.Reader(config.OCR_LANGUAGES, gpu=False)

    results = reader.readtext(image_path, detail=0, paragraph=True)
    return "\n".join(results).strip()


def process_single_image(args: tuple) -> dict:
    """Process a single image - used for parallel processing."""
    image_path, msg_id, engine = args

    result = {
        "msg_id": msg_id,
        "image_path": image_path,
        "ocr_text": "",
        "error": None,
    }

    try:
        if engine == "tesseract":
            result["ocr_text"] = ocr_with_tesseract(image_path)
        else:
            result["ocr_text"] = ocr_with_easyocr(image_path)
    except Exception as e:
        result["error"] = str(e)

    return result


class ImageProcessor:
    """Batch OCR processor for trade images."""

    def __init__(self, engine: str = None):
        self.engine = engine or config.OCR_ENGINE
        self.results_file = config.OUTPUT_DIR / "ocr_results.json"
        self.easyocr_reader = None

    def _init_easyocr(self):
        """Initialize EasyOCR reader (heavy, do once)."""
        if self.engine == "easyocr" and self.easyocr_reader is None:
            import easyocr
            self.easyocr_reader = easyocr.Reader(config.OCR_LANGUAGES, gpu=False)

    def process_all_images(self, messages: list = None) -> list:
        """
        Process all images from scraped messages.
        If messages is None, loads from the messages JSON file.
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
                image_tasks.append((msg["image_path"], msg["id"], self.engine))

        if not image_tasks:
            print("No images found to process.")
            return []

        print(f"Processing {len(image_tasks)} images with {self.engine}...")

        # Load existing results to support resume
        existing_results = self._load_existing_results()
        processed_ids = {r["msg_id"] for r in existing_results}

        # Filter out already processed
        remaining = [t for t in image_tasks if t[1] not in processed_ids]
        if remaining:
            print(f"  Skipping {len(image_tasks) - len(remaining)} already processed images")
        else:
            print("  All images already processed!")
            return existing_results

        results = list(existing_results)

        if self.engine == "easyocr":
            # EasyOCR doesn't parallelize well, process sequentially
            self._init_easyocr()
            for image_path, msg_id, engine in tqdm(remaining, desc="OCR"):
                try:
                    text = ocr_with_easyocr(image_path, reader=self.easyocr_reader)
                    results.append({
                        "msg_id": msg_id,
                        "image_path": image_path,
                        "ocr_text": text,
                        "error": None,
                    })
                except Exception as e:
                    results.append({
                        "msg_id": msg_id,
                        "image_path": image_path,
                        "ocr_text": "",
                        "error": str(e),
                    })
                # Save progress every 50 images
                if len(results) % 50 == 0:
                    self._save_results(results)
        else:
            # Tesseract can be parallelized
            workers = min(config.OCR_WORKERS, len(remaining))
            with ProcessPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(process_single_image, task): task
                    for task in remaining
                }
                for future in tqdm(
                    as_completed(futures), total=len(futures), desc="OCR"
                ):
                    result = future.result()
                    results.append(result)
                    if len(results) % 50 == 0:
                        self._save_results(results)

        self._save_results(results)
        errors = sum(1 for r in results if r.get("error"))
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
