"""
Trade data parser - extracts structured trade information
from OCR text and message text.
"""

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import config


@dataclass
class Trade:
    """Represents a single parsed trade."""
    msg_id: int = 0
    date: str = ""
    symbol: str = ""
    instrument: str = ""       # CE / PE / EQ / FUT
    strike_price: float = 0.0
    expiry: str = ""
    trade_type: str = ""       # BUY / SELL
    entry_price: float = 0.0
    target_price: float = 0.0
    stop_loss: float = 0.0
    exit_price: float = 0.0
    quantity: int = 0
    pnl: float = 0.0
    status: str = ""           # OPEN / CLOSED / TARGET_HIT / SL_HIT
    raw_text: str = ""
    source: str = ""           # "text" or "image"
    confidence: float = 0.0    # 0.0 to 1.0
    tags: list = field(default_factory=list)


class TradeParser:
    """Parses trade data from OCR text and message text."""

    # Patterns for Indian options market
    # Build dynamic pattern from config KNOWN_SYMBOLS
    SYMBOL_PATTERN = re.compile(
        r"\b(" + "|".join(re.escape(s) for s in sorted(config.KNOWN_SYMBOLS, key=len, reverse=True)) + r")\b",
        re.IGNORECASE,
    )
    STRIKE_PATTERN = re.compile(
        r"\b(\d{2,6})\s*(CE|PE|CALL|PUT)\b", re.IGNORECASE
    )
    # Catch ANY word before strike+CE/PE (e.g. "RELIANCE 2500 CE", "TATAPOWER 450 PE")
    SYMBOL_STRIKE_PATTERN = re.compile(
        r"\b([A-Z][A-Z0-9&\-]{1,20})\s+(\d{2,6})\s*(CE|PE|CALL|PUT)\b",
        re.IGNORECASE,
    )
    PRICE_PATTERN = re.compile(
        r"(?:@|at|price|cmp|around|near)\s*[:\-]?\s*(\d+\.?\d*)", re.IGNORECASE
    )
    TARGET_PATTERN = re.compile(
        r"(?:target|tgt|tp)\s*[:\-]?\s*(\d+\.?\d*)", re.IGNORECASE
    )
    STOPLOSS_PATTERN = re.compile(
        r"(?:sl|stop\s*loss|stoploss)\s*[:\-]?\s*(\d+\.?\d*)", re.IGNORECASE
    )
    ENTRY_PATTERN = re.compile(
        r"(?:entry|buy\s*(?:at|@|above)|bought\s*(?:at|@))\s*[:\-]?\s*(\d+\.?\d*)",
        re.IGNORECASE,
    )
    EXIT_PATTERN = re.compile(
        r"(?:exit|sold?\s*(?:at|@)|book(?:ed)?\s*(?:at|@)?)\s*[:\-]?\s*(\d+\.?\d*)",
        re.IGNORECASE,
    )
    EXPIRY_PATTERN = re.compile(
        r"\b(\d{1,2})\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b",
        re.IGNORECASE,
    )
    QUANTITY_PATTERN = re.compile(
        r"(?:qty|lot|quantity)\s*[:\-]?\s*(\d+)", re.IGNORECASE
    )

    def __init__(self):
        self.trades_file = config.OUTPUT_DIR / "trades.json"

    def parse_all(self, messages: list = None, ocr_results: list = None) -> list:
        """
        Parse trades from all messages and OCR results.
        Returns a list of Trade dataclass instances (as dicts).
        """
        if messages is None:
            msg_file = config.MESSAGES_DIR / "messages.json"
            if msg_file.exists():
                with open(msg_file, "r") as f:
                    messages = json.load(f)
            else:
                messages = []

        if ocr_results is None:
            ocr_file = config.OUTPUT_DIR / "ocr_results.json"
            if ocr_file.exists():
                with open(ocr_file, "r") as f:
                    ocr_results = json.load(f)
            else:
                ocr_results = []

        # Build OCR lookup by msg_id
        ocr_map = {r["msg_id"]: r["ocr_text"] for r in ocr_results if r.get("ocr_text")}

        trades = []
        for msg in messages:
            msg_id = msg["id"]
            date = msg.get("date", "")

            # Parse from message text
            if msg.get("text"):
                trade = self._parse_text(msg["text"], msg_id, date, source="text")
                if trade:
                    trades.append(trade)

            # Parse from OCR text
            if msg_id in ocr_map:
                trade = self._parse_text(ocr_map[msg_id], msg_id, date, source="image")
                if trade:
                    # If we already got a trade from text, merge image data
                    if trades and trades[-1]["msg_id"] == msg_id:
                        trades[-1] = self._merge_trades(trades[-1], trade)
                    else:
                        trades.append(trade)

        # Save trades
        self._save_trades(trades)
        print(f"Parsed {len(trades)} trades from {len(messages)} messages")
        print(f"Trades saved to: {self.trades_file}")

        return trades

    def _parse_text(self, text: str, msg_id: int, date: str, source: str) -> Optional[dict]:
        """Parse a single text block into a Trade."""
        if not text or len(text.strip()) < 5:
            return None

        trade = Trade(msg_id=msg_id, date=date, raw_text=text[:500], source=source)
        confidence = 0.0

        # Detect trade type
        text_lower = text.lower()
        is_buy = any(kw in text_lower for kw in config.BUY_KEYWORDS)
        is_sell = any(kw in text_lower for kw in config.SELL_KEYWORDS)

        if is_buy and not is_sell:
            trade.trade_type = "BUY"
            confidence += 0.2
        elif is_sell and not is_buy:
            trade.trade_type = "SELL"
            confidence += 0.2
        elif is_buy and is_sell:
            # Could be a complete trade (entry + exit)
            trade.trade_type = "BUY"
            trade.status = "CLOSED"
            confidence += 0.3

        # If no trade keywords found, skip
        if not is_buy and not is_sell:
            # Check if it looks like trade data anyway (has prices, symbols)
            has_numbers = bool(re.search(r"\d{2,}", text))
            if not has_numbers:
                return None

        # Extract symbol + strike + instrument together (e.g. "RELIANCE 2500 CE")
        combo_match = self.SYMBOL_STRIKE_PATTERN.search(text)
        if combo_match:
            sym = combo_match.group(1).upper()
            # Skip common non-symbol words
            skip_words = {"BUY", "SELL", "ABOVE", "BELOW", "NEAR", "AROUND", "TARGET", "ENTRY", "EXIT", "SL"}
            if sym not in skip_words:
                trade.symbol = sym
                trade.strike_price = float(combo_match.group(2))
                inst = combo_match.group(3).upper()
                trade.instrument = "CE" if inst in ("CE", "CALL") else "PE"
                confidence += 0.4

        # Fallback: try known symbols list
        if not trade.symbol:
            sym_match = self.SYMBOL_PATTERN.search(text)
            if sym_match:
                trade.symbol = sym_match.group(1).upper().replace(" ", "")
                confidence += 0.2

        # Fallback: try strike pattern alone
        if not trade.strike_price:
            strike_match = self.STRIKE_PATTERN.search(text)
            if strike_match:
                trade.strike_price = float(strike_match.group(1))
                inst = strike_match.group(2).upper()
                trade.instrument = "CE" if inst in ("CE", "CALL") else "PE"
                confidence += 0.2

        # Extract prices
        entry_match = self.ENTRY_PATTERN.search(text)
        if entry_match:
            trade.entry_price = float(entry_match.group(1))
            confidence += 0.1
        else:
            price_match = self.PRICE_PATTERN.search(text)
            if price_match:
                trade.entry_price = float(price_match.group(1))
                confidence += 0.05

        # Target
        target_match = self.TARGET_PATTERN.search(text)
        if target_match:
            trade.target_price = float(target_match.group(1))
            confidence += 0.05

        # Stop loss
        sl_match = self.STOPLOSS_PATTERN.search(text)
        if sl_match:
            trade.stop_loss = float(sl_match.group(1))
            confidence += 0.05

        # Exit price
        exit_match = self.EXIT_PATTERN.search(text)
        if exit_match:
            trade.exit_price = float(exit_match.group(1))
            confidence += 0.1

        # Quantity
        qty_match = self.QUANTITY_PATTERN.search(text)
        if qty_match:
            trade.quantity = int(qty_match.group(1))

        # Expiry
        expiry_match = self.EXPIRY_PATTERN.search(text)
        if expiry_match:
            trade.expiry = f"{expiry_match.group(1)} {expiry_match.group(2).title()}"

        # Determine status
        if not trade.status:
            if "target" in text_lower and ("hit" in text_lower or "done" in text_lower or "achieved" in text_lower):
                trade.status = "TARGET_HIT"
                confidence += 0.1
            elif "sl" in text_lower and "hit" in text_lower:
                trade.status = "SL_HIT"
                confidence += 0.1
            elif trade.exit_price > 0:
                trade.status = "CLOSED"
            else:
                trade.status = "OPEN"

        # Calculate P&L if we have entry and exit
        if trade.entry_price > 0 and trade.exit_price > 0:
            if trade.trade_type == "BUY":
                trade.pnl = trade.exit_price - trade.entry_price
            else:
                trade.pnl = trade.entry_price - trade.exit_price

        # Tags
        if "intraday" in text_lower:
            trade.tags.append("intraday")
        if "positional" in text_lower or "swing" in text_lower:
            trade.tags.append("positional")
        if "scalp" in text_lower:
            trade.tags.append("scalp")

        trade.confidence = min(confidence, 1.0)

        # Only return if we have some meaningful data
        if confidence < 0.1:
            return None

        return asdict(trade)

    def _merge_trades(self, text_trade: dict, image_trade: dict) -> dict:
        """Merge trade data from text and image sources, preferring non-empty values."""
        merged = dict(text_trade)
        for key, val in image_trade.items():
            if key in ("raw_text", "source", "msg_id", "date"):
                continue
            if val and not merged.get(key):
                merged[key] = val
            elif key == "confidence":
                merged[key] = max(merged.get(key, 0), val)
        merged["source"] = "text+image"
        return merged

    def _save_trades(self, trades: list):
        """Save parsed trades to JSON."""
        with open(self.trades_file, "w", encoding="utf-8") as f:
            json.dump(trades, f, indent=2, ensure_ascii=False)
