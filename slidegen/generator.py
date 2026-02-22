"""
Core slide generator engine.

Takes a list of SlideContent objects and produces HTML output,
handling batching (50 slides per batch), and rendering via templates.
"""
import os
from .config import SlideConfig
from .templates.base import html_head, html_foot, slide_footer
from .templates.cover import render_cover
from .templates.toc import render_toc
from .templates.comparison import render_comparison
from .templates.list_feature import render_list_feature
from .templates.section_break import render_section_break
from .templates.quote import render_quote
from .templates.data_viz import render_data_viz
from .templates.timeline import render_timeline
from .templates.faq import render_faq
from .templates.summary import render_summary
from .templates.guideline import render_guideline
from .templates.table_slide import render_table
from .templates.two_column import render_two_column


# Registry mapping slide_type -> renderer
RENDERERS = {
    "cover": render_cover,
    "toc": render_toc,
    "comparison": render_comparison,
    "list_feature": render_list_feature,
    "section_break": render_section_break,
    "quote": render_quote,
    "data_viz": render_data_viz,
    "timeline": render_timeline,
    "faq": render_faq,
    "summary": render_summary,
    "guideline": render_guideline,
    "table": render_table,
    "two_column": render_two_column,
}


def render_slide(slide, config=None):
    """Render a single slide to HTML based on its type."""
    renderer = RENDERERS.get(slide.slide_type)
    if renderer is None:
        # Fallback: render as list_feature
        renderer = render_list_feature
    return renderer(slide, config)


def generate_html(slides, title="Presentation", config=None, output_dir=None):
    """
    Generate a complete HTML slide deck from a list of SlideContent objects.

    Args:
        slides: List of SlideContent objects
        title: Presentation title (used in <title> tag)
        config: SlideConfig instance (optional, uses defaults)
        output_dir: Directory to write output files (optional)

    Returns:
        List of (filename, html_content) tuples
    """
    if config is None:
        config = SlideConfig()

    batch_size = config.batch_size
    total_slides = len(slides)
    batches = []

    for batch_start in range(0, total_slides, batch_size):
        batch_end = min(batch_start + batch_size, total_slides)
        batch_slides = slides[batch_start:batch_end]
        batch_num = (batch_start // batch_size) + 1

        slides_html = ""
        for slide in batch_slides:
            slides_html += render_slide(slide, config)

        if batch_num == 1:
            # First batch: full HTML document
            html = html_head(title, config) + slides_html + html_foot()
            filename = f"{_slugify(title)}_slides.html"
        else:
            # Subsequent batches: just the slides
            html = f"<!-- Batch {batch_num}: Slides {batch_start + 1}-{batch_end} -->\n"
            html += slides_html
            html += f"\n<!-- END Batch {batch_num} -->\n"
            filename = f"{_slugify(title)}_slides_batch{batch_num}.html"

        batches.append((filename, html))

    # Write to disk if output_dir provided
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        for filename, html in batches:
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  Written: {filepath}")

    return batches


def generate_single_html(slides, title="Presentation", config=None):
    """
    Generate a single combined HTML file (no batching).
    Useful for smaller decks or when you want one file.

    Returns:
        str: Complete HTML content
    """
    if config is None:
        config = SlideConfig()

    slides_html = ""
    for slide in slides:
        slides_html += render_slide(slide, config)

    return html_head(title, config) + slides_html + html_foot()


def _slugify(text):
    """Convert text to a safe filename slug."""
    slug = text.lower().strip()
    slug = slug.replace(" ", "_").replace("-", "_")
    return "".join(c for c in slug if c.isalnum() or c == "_")[:60]
