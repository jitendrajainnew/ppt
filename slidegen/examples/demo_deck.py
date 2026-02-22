"""
Demo slide deck - showcases all slide types available in SlideGen.
"""
from slidegen.models import SlideContent, CardItem, ComparisonItem, TOCItem, FAQItem, StatItem


def build_demo_slides():
    """Build a demo presentation showcasing all slide types."""
    slides = []

    # Slide 1: Cover
    slides.append(SlideContent(
        slide_number=1,
        slide_type="cover",
        title="SlideGen",
        subtitle="Beautiful HTML Presentations",
        description="A reusable tool for generating print-ready, professionally designed slide decks from structured data.",
        icon="ri-slideshow-3-line",
        items=[
            CardItem(title="Templates", icon="ri-layout-3-line"),
            CardItem(title="Print-Ready", icon="ri-printer-line"),
            CardItem(title="Customizable", icon="ri-palette-line"),
            CardItem(title="Fast", icon="ri-rocket-line"),
        ],
    ))

    # Slide 2: Table of Contents
    slides.append(SlideContent(
        slide_number=2,
        slide_type="toc",
        title="What's Inside",
        subtitle="Slide Types",
        items=[
            TOCItem(number=1, title="Cover Slides", description="Title and closing slides with decorative elements"),
            TOCItem(number=2, title="Content Slides", description="Feature lists, comparisons, and two-column layouts"),
            TOCItem(number=3, title="Data Slides", description="Stats, tables, progress bars, and visualizations"),
            TOCItem(number=4, title="Special Slides", description="Quotes, FAQs, timelines, and section breaks"),
        ],
        extra={"quote": "Great design is not just what it looks like. It's how it works."},
    ))

    # Slide 3: Section Break
    slides.append(SlideContent(
        slide_number=3,
        slide_type="section_break",
        title="Content Slide Types",
        subtitle="Lists, Features & Comparisons",
        description="The building blocks for presenting information clearly.",
        icon="ri-layout-grid-line",
        extra={"section_number": 1},
    ))

    # Slide 4: List/Feature
    slides.append(SlideContent(
        slide_number=4,
        slide_type="list_feature",
        title="Available Slide Templates",
        description="SlideGen includes 13 built-in slide types for any presentation need.",
        columns=3,
        items=[
            CardItem(title="Cover", icon="ri-home-4-line", badge="Essential",
                     points=["Gradient text titles", "Decorative blurred elements", "Icon showcase row"]),
            CardItem(title="Table of Contents", icon="ri-list-ordered", badge="Navigation",
                     points=["Numbered sections", "Color-coded items", "Optional quote block"]),
            CardItem(title="Comparison", icon="ri-scales-3-line", badge="Analysis",
                     points=["2 or 3 column layout", "Progress bar metrics", "Summary row"]),
            CardItem(title="Feature List", icon="ri-checkbox-circle-line", badge="Content",
                     points=["Grid card layout", "Icons and badges", "Bottom section"]),
            CardItem(title="Data Viz", icon="ri-bar-chart-grouped-line", badge="Metrics",
                     points=["Stat cards", "Progress bars", "Insight boxes"]),
            CardItem(title="Timeline", icon="ri-time-line", badge="Process",
                     points=["Step-by-step flow", "Connected nodes", "Summary box"]),
        ],
    ))

    # Slide 5: Comparison
    slides.append(SlideContent(
        slide_number=5,
        slide_type="comparison",
        title="Comparison: HTML vs PPTX Slides",
        description="Why HTML-based presentations offer significant advantages.",
        columns=2,
        items=[
            ComparisonItem(
                title="HTML Slides",
                icon="ri-html5-line",
                badge="Recommended",
                points=[
                    "Full CSS styling control",
                    "Print to PDF natively",
                    "Version control friendly",
                    "No special software needed",
                    "Responsive and accessible",
                ],
                metrics={"Flexibility": 95, "Print Quality": 90},
            ),
            ComparisonItem(
                title="PPTX Slides",
                icon="ri-file-ppt-line",
                badge="Traditional",
                points=[
                    "Familiar editing interface",
                    "Animation support",
                    "Embedded media playback",
                    "Corporate template ecosystem",
                    "Offline presentation mode",
                ],
                metrics={"Flexibility": 60, "Print Quality": 75},
            ),
        ],
        extra={"summary_items": [
            {"label": "Best For", "values": ["Technical content", "Data-heavy decks"]},
            {"label": "Output", "values": ["HTML + PDF", "PPTX"]},
            {"label": "Customization", "values": ["Unlimited CSS", "Theme-based"]},
        ]},
    ))

    # Slide 6: Data Viz
    slides.append(SlideContent(
        slide_number=6,
        slide_type="data_viz",
        title="Project Statistics",
        description="Key metrics from the SlideGen project.",
        items=[
            StatItem(value="13", label="Slide Types", icon="ri-layout-3-line"),
            StatItem(value="50+", label="CSS Components", icon="ri-palette-line"),
            StatItem(value="100%", label="Print Ready", icon="ri-printer-line"),
            StatItem(value="0", label="Dependencies", icon="ri-box-3-line"),
        ],
        extra={
            "bars": [
                {"label": "Code Reusability", "value": 95, "display": "95%"},
                {"label": "Print Fidelity", "value": 90, "display": "90%"},
                {"label": "Customizability", "value": 88, "display": "88%"},
                {"label": "Ease of Use", "value": 85, "display": "85%"},
            ],
            "insight": "SlideGen produces presentations that are pixel-perfect in both browser and PDF output, with zero external dependencies beyond Python.",
        },
    ))

    # Slide 7: Timeline
    slides.append(SlideContent(
        slide_number=7,
        slide_type="timeline",
        title="How to Create a Deck",
        description="Five simple steps from content to presentation.",
        items=[
            CardItem(title="Define Content", description="Structure your data as SlideContent objects", label="Step 1", icon="ri-draft-line"),
            CardItem(title="Choose Types", description="Pick the right slide type for each section", label="Step 2", icon="ri-layout-3-line"),
            CardItem(title="Configure", description="Set colors, footer, and branding", label="Step 3", icon="ri-settings-3-line"),
            CardItem(title="Generate", description="Run the generator to produce HTML", label="Step 4", icon="ri-code-line"),
            CardItem(title="Export", description="Open in browser and print to PDF", label="Step 5", icon="ri-file-pdf-line"),
        ],
        extra={"summary": "The entire process takes seconds. Slides are generated instantly from your structured data."},
    ))

    # Slide 8: Guideline
    slides.append(SlideContent(
        slide_number=8,
        slide_type="guideline",
        title="Best Practices for Slide Content",
        description="Follow these guidelines for maximum impact.",
        columns=2,
        items=[
            CardItem(title="Keep It Simple", icon="ri-focus-3-line",
                     points=["One core idea per slide", "Limit to 6 bullet points", "Use short sentences"],
                     extra={"note": "Simplicity is the ultimate sophistication."}),
            CardItem(title="Use Visuals", icon="ri-image-line",
                     points=["Stats and metrics", "Progress indicators", "Icon-driven layouts"],
                     extra={"note": "Visual information is processed 60,000x faster than text."}),
            CardItem(title="Tell a Story", icon="ri-book-open-line",
                     points=["Logical flow", "Section breaks", "Build toward conclusion"],
                     extra={"note": "Structure your deck as a narrative arc."}),
            CardItem(title="Design for Print", icon="ri-printer-line",
                     points=["Test PDF output", "Check page breaks", "Verify color fidelity"],
                     extra={"note": "Always preview the printed version before sharing."}),
        ],
        extra={"best_practices": [
            "Test in multiple browsers before export",
            "Use the print button to verify layout",
            "Keep consistent color usage across slides",
            "Limit text density - let content breathe",
        ]},
    ))

    # Slide 9: Table
    slides.append(SlideContent(
        slide_number=9,
        slide_type="table",
        title="Slide Type Reference",
        description="Quick reference for all available slide types and their use cases.",
        extra={
            "headers": ["Type", "Best For", "Columns", "Key Features"],
            "rows": [
                ["Cover", "Title / Closing", "Center", "Gradient text, decoration blurs"],
                ["TOC", "Navigation", "2-col grid", "Numbered items, quote block"],
                ["Comparison", "A vs B analysis", "2-3 cols", "Progress bars, summary row"],
                ["List/Feature", "Feature showcase", "2-3 cols", "Icon cards, badges"],
                ["Data Viz", "Statistics", "Up to 4 cols", "Stat cards, bar charts"],
                ["Timeline", "Processes", "Up to 5 steps", "Connected flow"],
                ["Guideline", "Best practices", "2-3 cols", "Numbered steps, notes"],
                ["Table", "Structured data", "Full width", "Sortable rows"],
                ["Two Column", "Content + sidebar", "3-col split", "Sidebar panels"],
                ["Quote", "Key messages", "Center", "Quote card, author"],
                ["FAQ", "Q&A format", "Full width", "Question/answer pairs"],
                ["Section Break", "Transitions", "Center", "Large gradient title"],
                ["Summary", "Key takeaways", "2-3 cols", "Points + outlook sidebar"],
            ],
            "insight": "Mix and match these types to create a compelling narrative flow. Start with a cover, use section breaks between topics, and end with a summary.",
        },
    ))

    # Slide 10: Two Column
    slides.append(SlideContent(
        slide_number=10,
        slide_type="two_column",
        title="Customization Options",
        description="SlideGen is fully configurable to match your brand.",
        items=[
            CardItem(title="Colors & Gradients", icon="ri-palette-line",
                     points=["Custom gradient start/mid/end colors", "8 accent color palettes", "Full Tailwind color access"]),
            CardItem(title="Footer & Branding", icon="ri-user-star-line",
                     points=["Custom author name and link", "Configurable icon", "Page numbering"]),
            CardItem(title="Layout Control", icon="ri-layout-line",
                     points=["Adjustable slide dimensions", "Configurable batch size", "Print margin control"]),
        ],
        extra={
            "sidebar_title": "Quick Config",
            "sidebar_items": [
                {"title": "SlideConfig", "description": "Pass custom settings for colors, footer, layout", "icon": "ri-settings-3-line"},
                {"title": "Per-Slide Override", "description": "Each slide can use its own column count and items", "icon": "ri-pencil-line"},
            ],
        },
    ))

    # Slide 11: Quote
    slides.append(SlideContent(
        slide_number=11,
        slide_type="quote",
        title="Design Philosophy",
        description="The best slides are the ones that make complex ideas feel simple. Every element should earn its place on the page.",
        icon="ri-double-quotes-l",
        items=[
            CardItem(title="Print-first design ensures quality at every output size"),
            CardItem(title="Structured data means reproducible, versionable presentations"),
            CardItem(title="Zero dependencies keeps the tool lightweight and portable"),
        ],
        extra={"author": "SlideGen", "role": "Design Principles"},
    ))

    # Slide 12: FAQ
    slides.append(SlideContent(
        slide_number=12,
        slide_type="faq",
        title="Frequently Asked Questions",
        description="Common questions about using SlideGen.",
        items=[
            FAQItem(question="How do I create a new presentation?",
                    answer="Create a Python script that defines a build_slides() function returning a list of SlideContent objects, then run: python -m slidegen generate your_script.py"),
            FAQItem(question="Can I export to PDF?",
                    answer="Yes! Open the generated HTML in any browser and click the print button (or Ctrl+P). The slides are designed to print perfectly."),
            FAQItem(question="How do I customize the colors?",
                    answer="Pass a SlideConfig object with custom gradient_start, gradient_mid, gradient_end values to the generator."),
            FAQItem(question="What about large presentations?",
                    answer="SlideGen automatically batches output into 50-slide chunks. Use --single flag to force a single file output."),
        ],
    ))

    # Slide 13: Summary
    slides.append(SlideContent(
        slide_number=13,
        slide_type="summary",
        title="Key Takeaways",
        description="What makes SlideGen the right choice for your presentations.",
        items=[
            CardItem(title="13 Slide Types", description="Cover every presentation need from stats to FAQs.", icon="ri-layout-3-line"),
            CardItem(title="Print-Perfect Output", description="Designed for PDF export from the ground up.", icon="ri-printer-line"),
            CardItem(title="Pure Python", description="No JS frameworks, no build steps, no dependencies.", icon="ri-code-s-slash-line"),
            CardItem(title="Fully Customizable", description="Colors, layout, footer - everything is configurable.", icon="ri-palette-line"),
        ],
        extra={
            "outlook_title": "What's Next",
            "outlook": [
                {"icon": "ri-rocket-line", "text": "Theme presets for different industries"},
                {"icon": "ri-magic-line", "text": "AI-powered content structuring"},
                {"icon": "ri-global-line", "text": "Multi-language support"},
            ],
        },
    ))

    # Slide 14: Closing Cover
    slides.append(SlideContent(
        slide_number=14,
        slide_type="cover",
        title="Start Creating",
        subtitle="Your Next Presentation",
        description="python -m slidegen demo",
        icon="ri-rocket-2-line",
        extra={"cta": "Build something beautiful."},
    ))

    return slides
