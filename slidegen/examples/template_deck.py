"""
Template slide deck - copy this file to create your own presentations.

Usage:
    1. Copy this file: cp template_deck.py my_topic.py
    2. Edit the slides in build_slides()
    3. Generate: python -m slidegen generate my_topic.py --title "My Topic"

Available slide types:
    cover         - Title/closing slides with decorative elements
    toc           - Table of Contents with numbered sections
    section_break - Transition dividers between sections
    list_feature  - Feature/principle cards in a grid
    comparison    - Side-by-side column comparisons
    data_viz      - Statistics, metrics, and bar charts
    timeline      - Step-by-step process flow
    guideline     - Numbered strategy/best-practice steps
    table         - Full-width data tables
    two_column    - Main content + sidebar layout
    quote         - Large quote with attribution
    faq           - Question and answer pairs
    summary       - Key takeaways with optional outlook sidebar
"""
from slidegen.models import (
    SlideContent, CardItem, ComparisonItem, TOCItem,
    FAQItem, StatItem, TimelineItem, QuoteData,
)


def build_slides():
    """Build your presentation slides. Return a list of SlideContent objects."""
    slides = []

    # === SLIDE 1: COVER ===
    slides.append(SlideContent(
        slide_number=1,
        slide_type="cover",
        title="Your Presentation Title",
        subtitle="A Compelling Subtitle",
        description="Brief description of what this presentation covers.",
        icon="ri-presentation-line",  # Remixicon class name
        items=[
            # Optional icon row below the title
            CardItem(title="Topic 1", icon="ri-lightbulb-line"),
            CardItem(title="Topic 2", icon="ri-bar-chart-line"),
            CardItem(title="Topic 3", icon="ri-rocket-line"),
        ],
    ))

    # === SLIDE 2: TABLE OF CONTENTS ===
    slides.append(SlideContent(
        slide_number=2,
        slide_type="toc",
        title="Agenda",
        subtitle="Overview",
        items=[
            TOCItem(number=1, title="Introduction", description="Background and context"),
            TOCItem(number=2, title="Core Analysis", description="Key findings"),
            TOCItem(number=3, title="Recommendations", description="Actionable insights"),
            TOCItem(number=4, title="Conclusion", description="Summary and next steps"),
        ],
        extra={"quote": "Optional inspirational quote here."},
    ))

    # === SLIDE 3: SECTION BREAK ===
    slides.append(SlideContent(
        slide_number=3,
        slide_type="section_break",
        title="Section Title",
        subtitle="Optional subtitle for context",
        icon="ri-bookmark-line",
        extra={"section_number": 1},
    ))

    # === SLIDE 4: LIST/FEATURE ===
    slides.append(SlideContent(
        slide_number=4,
        slide_type="list_feature",
        title="Key Features",
        description="What makes this topic important.",
        columns=3,  # 2 or 3
        items=[
            CardItem(
                title="Feature One",
                icon="ri-checkbox-circle-line",
                badge="Core",  # Optional badge
                points=["Point A", "Point B", "Point C"],
                extra={"note": "Optional note box text"},
            ),
            CardItem(
                title="Feature Two",
                icon="ri-shield-check-line",
                points=["Point D", "Point E"],
            ),
            CardItem(
                title="Feature Three",
                icon="ri-line-chart-line",
                points=["Point F", "Point G"],
            ),
        ],
        extra={
            # Optional bottom section
            "bottom_title": "Summary",
            "bottom_items": [
                {"title": "Label 1", "desc": "Value 1"},
                {"title": "Label 2", "desc": "Value 2"},
            ],
        },
    ))

    # === SLIDE 5: COMPARISON ===
    slides.append(SlideContent(
        slide_number=5,
        slide_type="comparison",
        title="Option A vs Option B",
        description="How they stack up.",
        columns=2,
        items=[
            ComparisonItem(
                title="Option A",
                icon="ri-star-line",
                badge="Recommended",
                points=["Advantage 1", "Advantage 2", "Advantage 3"],
                metrics={"Performance": 85, "Cost": 70},
            ),
            ComparisonItem(
                title="Option B",
                icon="ri-star-half-line",
                points=["Advantage 1", "Advantage 2"],
                metrics={"Performance": 65, "Cost": 90},
            ),
        ],
    ))

    # === SLIDE 6: DATA VISUALIZATION ===
    slides.append(SlideContent(
        slide_number=6,
        slide_type="data_viz",
        title="Key Metrics",
        description="Important numbers at a glance.",
        items=[
            StatItem(value="42%", label="Growth Rate", icon="ri-arrow-up-line"),
            StatItem(value="98", label="Satisfaction Score", icon="ri-heart-line"),
            StatItem(value="$2.4M", label="Revenue", icon="ri-money-dollar-circle-line"),
        ],
        extra={
            "bars": [
                {"label": "Q1 Performance", "value": 78, "display": "78%"},
                {"label": "Q2 Performance", "value": 85, "display": "85%"},
            ],
            "insight": "Key insight about what these numbers mean.",
        },
    ))

    # === SLIDE 7: TIMELINE ===
    slides.append(SlideContent(
        slide_number=7,
        slide_type="timeline",
        title="Implementation Roadmap",
        description="The path from planning to launch.",
        items=[
            CardItem(title="Research", description="Gather requirements", label="Phase 1", icon="ri-search-line"),
            CardItem(title="Design", description="Create prototypes", label="Phase 2", icon="ri-pencil-ruler-line"),
            CardItem(title="Build", description="Develop solution", label="Phase 3", icon="ri-code-line"),
            CardItem(title="Launch", description="Deploy and monitor", label="Phase 4", icon="ri-rocket-line"),
        ],
    ))

    # === SLIDE 8: TABLE ===
    slides.append(SlideContent(
        slide_number=8,
        slide_type="table",
        title="Detailed Comparison",
        extra={
            "headers": ["Feature", "Plan A", "Plan B", "Plan C"],
            "rows": [
                ["Storage", "10 GB", "50 GB", "Unlimited"],
                ["Users", "5", "25", "Unlimited"],
                ["Support", "Email", "Priority", "Dedicated"],
                ["Price", "$9/mo", "$29/mo", "$99/mo"],
            ],
            "insight": "Plan B offers the best value for most teams.",
        },
    ))

    # === SLIDE 9: QUOTE ===
    slides.append(SlideContent(
        slide_number=9,
        slide_type="quote",
        title="Words of Wisdom",
        description="The only way to do great work is to love what you do.",
        extra={"author": "Steve Jobs", "role": "Co-founder, Apple"},
    ))

    # === SLIDE 10: FAQ ===
    slides.append(SlideContent(
        slide_number=10,
        slide_type="faq",
        title="Common Questions",
        items=[
            FAQItem(question="What is this about?", answer="A comprehensive overview of the topic."),
            FAQItem(question="How do I get started?", answer="Follow the steps in the timeline section."),
        ],
    ))

    # === SLIDE 11: SUMMARY ===
    slides.append(SlideContent(
        slide_number=11,
        slide_type="summary",
        title="Key Takeaways",
        items=[
            CardItem(title="Point 1", description="Summary of first key point.", icon="ri-check-double-line"),
            CardItem(title="Point 2", description="Summary of second key point.", icon="ri-check-double-line"),
            CardItem(title="Point 3", description="Summary of third key point.", icon="ri-check-double-line"),
        ],
        extra={
            "outlook_title": "Next Steps",
            "outlook": [
                {"icon": "ri-arrow-right-s-line", "text": "Action item 1"},
                {"icon": "ri-arrow-right-s-line", "text": "Action item 2"},
            ],
        },
    ))

    # === SLIDE 12: CLOSING COVER ===
    slides.append(SlideContent(
        slide_number=12,
        slide_type="cover",
        title="Thank You",
        subtitle="Questions?",
        description="Contact: your@email.com",
        icon="ri-hand-heart-line",
        extra={"cta": "Let's build something great together."},
    ))

    return slides
