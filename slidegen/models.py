"""
Data models for slide content.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SlideContent:
    """Base content for any slide."""
    slide_number: int
    slide_type: str  # cover, toc, comparison, list_feature, guideline, summary, section_break, quote, data_viz, timeline, faq, case_study
    title: str = ""
    subtitle: str = ""
    description: str = ""
    items: list = field(default_factory=list)
    columns: int = 2
    icon: str = ""
    extra: dict = field(default_factory=dict)


@dataclass
class CardItem:
    """A card/item within a slide."""
    title: str
    description: str = ""
    icon: str = ""
    points: list = field(default_factory=list)
    badge: str = ""
    label: str = ""
    color_index: int = 0
    extra: dict = field(default_factory=dict)


@dataclass
class ComparisonItem:
    """An item in a comparison slide."""
    title: str
    subtitle: str = ""
    icon: str = ""
    points: list = field(default_factory=list)
    badge: str = ""
    color_index: int = 0
    metrics: dict = field(default_factory=dict)


@dataclass
class TOCItem:
    """Table of contents entry."""
    number: int
    title: str
    description: str = ""
    color_index: int = 0


@dataclass
class TimelineItem:
    """Timeline entry."""
    label: str
    title: str
    description: str = ""
    icon: str = ""
    color_index: int = 0


@dataclass
class FAQItem:
    """FAQ entry."""
    question: str
    answer: str


@dataclass
class StatItem:
    """A statistic/metric display."""
    value: str
    label: str
    icon: str = ""
    color_index: int = 0


@dataclass
class QuoteData:
    """Quote content."""
    text: str
    author: str = ""
    role: str = ""


@dataclass
class TableData:
    """Table content."""
    headers: list = field(default_factory=list)
    rows: list = field(default_factory=list)


@dataclass
class Presentation:
    """Full presentation data."""
    title: str
    subtitle: str = ""
    author: str = ""
    slides: list = field(default_factory=list)
    theme: str = "default"
