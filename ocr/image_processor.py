"""
OCR pipeline for extracting text from trade screenshot images.
Default engine: rapidocr (lightweight, no PyTorch, no system deps).
Optional: tesseract, easyocr, surya (require extra installs).
"""

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
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

    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    img = img.convert("L")

    min_width = 800
    if img.width < min_width:
        ratio = min_width / img.width
        img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    img = img.filter(ImageFilter.SHARPEN)

    return img


def ocr_with_rapidocr(image_path: str, engine=None) -> str:
    """Extract text using RapidOCR (lightweight, ONNX-based)."""
    from rapidocr_onnxruntime import RapidOCR

    if engine is None:
        engine = RapidOCR()

    img = preprocess_image(image_path)
    # RapidOCR accepts PIL images
    result, _ = engine(img)
    if result is None:
        return ""
    # result is list of [box, text, confidence]
    lines = [item[1] for item in result]
    return "\n".join(lines).strip()


def ocr_with_tesseract(image_path: str) -> str:
    """Extract text using Tesseract OCR (requires system tesseract)."""
    import pytesseract

    img = preprocess_image(image_path)
    custom_config = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(img, config=custom_config)
    return text.strip()


class ImageProcessor:
    """Batch OCR processor for trade images."""

    def __init__(self, engine: str = None):
        self.engine = engine or config.OCR_ENGINE
        self.results_file = config.OUTPUT_DIR / "ocr_results.json"
        self.ocr_engine = None

    def _init_engine(self):
        """Initialize the OCR engine once."""
        if self.ocr_engine is not None:
            return

        if self.engine == "rapidocr":
            from rapidocr_onnxruntime import RapidOCR
            self.ocr_engine = RapidOCR()
        elif self.engine == "tesseract":
            self.ocr_engine = "tesseract"  # placeholder, pytesseract has no init

    def _ocr_single(self, image_path: str) -> str:
        """Run OCR on a single image."""
        if self.engine == "rapidocr":
            return ocr_with_rapidocr(image_path, engine=self.ocr_engine)
        elif self.engine == "tesseract":
            return ocr_with_tesseract(image_path)
        else:
            raise ValueError(f"Unknown OCR engine: {self.engine}")

    def process_all_images(self, messages: list = None) -> list:
        """
        Process all images from scraped messages.
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

        print(f"Processing {len(image_tasks)} images with {self.engine}...")

        # Load existing results to support resume
        existing_results = self._load_existing_results()
        processed_ids = {r["msg_id"] for r in existing_results}

        remaining = [t for t in image_tasks if t[1] not in processed_ids]
        if remaining:
            print(f"  Skipping {len(image_tasks) - len(remaining)} already processed images")
        else:
            print("  All images already processed!")
            return existing_results

        # Init engine
        self._init_engine()

        results = list(existing_results)

        for image_path, msg_id in tqdm(remaining, desc="OCR"):
            try:
                text = self._ocr_single(image_path)
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
