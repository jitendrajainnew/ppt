"""
FAQ slide template.
"""
from .base import slide_footer


def render_faq(slide, config=None):
    """Render an FAQ slide."""
    n = slide.slide_number
    title = slide.title or "Frequently Asked Questions"
    description = slide.description or ""

    items_html = ""
    for i, item in enumerate(slide.items):
        q = item.question if hasattr(item, 'question') else item.title if hasattr(item, 'title') else str(item)
        a = item.answer if hasattr(item, 'answer') else item.description if hasattr(item, 'description') else ""

        items_html += f'''<div class="border border-gray-100 rounded-xl p-5 card">
                <div class="flex items-start faq-q-icon">
                    <h3 class="text-base font-semibold text-gray-800">{q}</h3>
                </div>
                <div class="flex items-start faq-a-icon mt-3">
                    <p class="text-sm text-gray-600 leading-relaxed">{a}</p>
                </div>
            </div>'''

    return f'''<!-- Slide {n}: FAQ -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid grid-cols-1 gap-4">
            {items_html}
        </div>
    </div>

{slide_footer(n, config)}
</div>
'''
