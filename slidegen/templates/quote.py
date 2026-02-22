"""
Quote slide template.
"""
from .base import slide_footer


def render_quote(slide, config=None):
    """Render a quote slide."""
    n = slide.slide_number
    title = slide.title or ""
    quote_text = slide.description or ""
    author = slide.extra.get("author", "")
    role = slide.extra.get("role", "")
    icon = slide.icon or "ri-double-quotes-l"

    # Additional context points
    points_html = ""
    if slide.items:
        pts = ""
        for item in slide.items:
            t = item.title if hasattr(item, 'title') else str(item)
            pts += f'''<div class="flex items-start space-x-3 mb-3">
                    <i class="ri-arrow-right-s-line text-indigo-500 mt-0.5 flex-shrink-0"></i>
                    <span class="text-gray-700">{t}</span>
                </div>'''
        points_html = f'''<div class="mt-8 grid grid-cols-1 gap-1 max-w-2xl mx-auto text-left">
            {pts}
        </div>'''

    return f'''<!-- Slide {n}: Quote -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper flex flex-col justify-center items-center">
        {"<h1 class='text-3xl font-bold text-gray-800 mb-8'>" + title + "</h1>" if title else ""}

        <div class="relative accent-gradient rounded-2xl p-10 max-w-3xl w-full">
            <div class="quote-left-bar"></div>
            <div class="ml-4">
                <i class="{icon} text-4xl text-indigo-400 mb-4 block"></i>
                <p class="text-2xl text-gray-800 italic leading-relaxed font-medium">{quote_text}</p>
                {"<div class='mt-6'><span class='font-semibold text-gray-800'>" + author + "</span>" + ("<span class='text-gray-500 ml-2'>" + role + "</span>" if role else "") + "</div>" if author else ""}
            </div>
        </div>

        {points_html}
    </div>

{slide_footer(n, config)}
</div>
'''
