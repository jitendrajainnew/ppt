"""
Telegram channel scraper using Telethon.
Downloads all messages (text + images) from a public channel.
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from tqdm import tqdm

import config


class TelegramScraper:
    """Scrapes messages and media from a Telegram channel."""

    def __init__(self):
        if not config.TELEGRAM_API_ID or not config.TELEGRAM_API_HASH:
            print("ERROR: Set TELEGRAM_API_ID and TELEGRAM_API_HASH in your .env file")
            print("Get them from https://my.telegram.org")
            sys.exit(1)

        self.client = TelegramClient(
            str(config.DATA_DIR / "scraper_session"),
            int(config.TELEGRAM_API_ID),
            config.TELEGRAM_API_HASH,
        )
        self.channel = config.TELEGRAM_CHANNEL
        self.messages_file = config.MESSAGES_DIR / "messages.json"

    async def connect(self):
        """Connect and authenticate with Telegram."""
        await self.client.start(phone=config.TELEGRAM_PHONE)
        print(f"Connected to Telegram as: {(await self.client.get_me()).first_name}")

    async def scrape_channel(self):
        """Download all messages and images from the channel."""
        await self.connect()

        entity = await self.client.get_entity(self.channel)
        print(f"Scraping channel: {entity.title}")

        messages_data = []
        image_count = 0
        total = 0

        # Get total message count for progress bar
        async for _ in self.client.iter_messages(entity, limit=1):
            pass

        limit = config.MAX_MESSAGES if config.MAX_MESSAGES > 0 else None
        pbar = tqdm(desc="Downloading messages", unit="msg")

        async for message in self.client.iter_messages(entity, limit=limit):
            total += 1
            pbar.update(1)

            msg_data = {
                "id": message.id,
                "date": message.date.isoformat() if message.date else None,
                "text": message.text or "",
                "has_media": message.media is not None,
                "media_type": None,
                "image_path": None,
                "reply_to": message.reply_to_msg_id if message.reply_to else None,
                "views": getattr(message, "views", None),
                "forwards": getattr(message, "forwards", None),
            }

            # Download images
            if message.media:
                if isinstance(message.media, MessageMediaPhoto):
                    msg_data["media_type"] = "photo"
                    img_path = config.IMAGES_DIR / f"msg_{message.id}.jpg"
                    await self.client.download_media(message, file=str(img_path))
                    msg_data["image_path"] = str(img_path)
                    image_count += 1

                elif isinstance(message.media, MessageMediaDocument):
                    mime = getattr(message.media.document, "mime_type", "")
                    if mime.startswith("image/"):
                        msg_data["media_type"] = "image_doc"
                        ext = mime.split("/")[-1].replace("jpeg", "jpg")
                        img_path = config.IMAGES_DIR / f"msg_{message.id}.{ext}"
                        await self.client.download_media(message, file=str(img_path))
                        msg_data["image_path"] = str(img_path)
                        image_count += 1
                    else:
                        msg_data["media_type"] = "document"

            messages_data.append(msg_data)

            # Save progress every batch
            if total % config.BATCH_SIZE == 0:
                self._save_messages(messages_data)

        pbar.close()

        # Final save
        self._save_messages(messages_data)
        await self.client.disconnect()

        print(f"\nDone! Scraped {total} messages, downloaded {image_count} images")
        print(f"Messages saved to: {self.messages_file}")
        print(f"Images saved to: {config.IMAGES_DIR}")

        return messages_data

    def _save_messages(self, messages_data):
        """Save messages to JSON file."""
        with open(self.messages_file, "w", encoding="utf-8") as f:
            json.dump(messages_data, f, indent=2, ensure_ascii=False, default=str)


class WebScraper:
    """
    Fallback scraper using the public web preview (t.me/s/channel).
    No API credentials needed, but limited to public channels.
    """

    def __init__(self):
        self.channel = config.TELEGRAM_CHANNEL
        self.base_url = f"https://t.me/s/{self.channel}"
        self.messages_file = config.MESSAGES_DIR / "messages.json"

    def scrape_channel(self):
        """Scrape public channel via web preview."""
        import requests
        from bs4 import BeautifulSoup

        messages_data = []
        before_id = None
        page = 0
        image_count = 0

        print(f"Scraping {self.base_url} via web preview...")
        pbar = tqdm(desc="Downloading pages", unit="page")

        while True:
            url = self.base_url
            if before_id:
                url = f"{self.base_url}?before={before_id}"

            resp = requests.get(url, timeout=30)
            if resp.status_code != 200:
                print(f"HTTP {resp.status_code} - stopping")
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            posts = soup.select(".tgme_widget_message_wrap")

            if not posts:
                break

            first_id = None
            for post in posts:
                msg_widget = post.select_one(".tgme_widget_message")
                if not msg_widget:
                    continue

                data_post = msg_widget.get("data-post", "")
                msg_id = int(data_post.split("/")[-1]) if "/" in data_post else 0

                if first_id is None or msg_id < first_id:
                    first_id = msg_id

                # Extract text
                text_el = post.select_one(".tgme_widget_message_text")
                text = text_el.get_text(separator="\n").strip() if text_el else ""

                # Extract date
                date_el = post.select_one(".tgme_widget_message_date time")
                date_str = date_el.get("datetime", "") if date_el else ""

                # Extract image
                image_path = None
                img_el = post.select_one(
                    ".tgme_widget_message_photo_wrap"
                )
                if img_el:
                    style = img_el.get("style", "")
                    # Extract URL from background-image style
                    if "background-image" in style:
                        img_url = style.split("url('")[-1].split("')")[0]
                        if img_url.startswith("http"):
                            img_file = config.IMAGES_DIR / f"msg_{msg_id}.jpg"
                            try:
                                img_resp = requests.get(img_url, timeout=30)
                                if img_resp.status_code == 200:
                                    img_file.write_bytes(img_resp.content)
                                    image_path = str(img_file)
                                    image_count += 1
                            except Exception as e:
                                print(f"  Failed to download image for msg {msg_id}: {e}")

                messages_data.append({
                    "id": msg_id,
                    "date": date_str,
                    "text": text,
                    "has_media": image_path is not None,
                    "media_type": "photo" if image_path else None,
                    "image_path": image_path,
                    "reply_to": None,
                    "views": None,
                    "forwards": None,
                })

            page += 1
            pbar.update(1)

            # Save progress
            if page % 5 == 0:
                self._save_messages(messages_data)

            # Move to older messages
            if first_id and first_id > 1:
                if before_id == first_id:
                    break  # No more messages
                before_id = first_id
            else:
                break

            # Rate limit
            import time
            time.sleep(1)

            if config.MAX_MESSAGES > 0 and len(messages_data) >= config.MAX_MESSAGES:
                break

        pbar.close()
        self._save_messages(messages_data)

        print(f"\nDone! Scraped {len(messages_data)} messages, downloaded {image_count} images")
        print(f"Messages saved to: {self.messages_file}")

        return messages_data

    def _save_messages(self, messages_data):
        """Save messages to JSON file."""
        with open(self.messages_file, "w", encoding="utf-8") as f:
            json.dump(messages_data, f, indent=2, ensure_ascii=False, default=str)


async def run_api_scraper():
    """Run the Telethon-based scraper."""
    scraper = TelegramScraper()
    return await scraper.scrape_channel()


def run_web_scraper():
    """Run the web-based fallback scraper."""
    scraper = WebScraper()
    return scraper.scrape_channel()
