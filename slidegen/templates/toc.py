"""
Table of Contents slide template.
"""
from .base import slide_footer


def render_toc(slide, config=None):
    """Render a Table of Contents slide."""
    n = slide.slide_number
    title = slide.title or "Table of Contents"
    subtitle = slide.subtitle or "Overview"

    color_fills = [
        "bg-blue-500", "bg-purple-500", "bg-green-500", "bg-indigo-500",
        "bg-pink-500", "bg-orange-500", "bg-teal-500", "bg-red-500"
    ]

    items_html = ""
    for i, item in enumerate(slide.items):
        num = item.number if hasattr(item, 'number') else i + 1
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') else ""
        color = color_fills[i % len(color_fills)]
        items_html += f'''<div class="card flex items-start space-x-4 p-4 rounded-lg cursor-pointer">
                <div class="rounded-full {color} text-white p-2 flex items-center justify-center w-10 h-10 flex-shrink-0">
                    <span class="text-xl font-bold">{num}</span>
                </div>
                <div>
                    <h3 class="text-xl font-semibold text-gray-800">{t}</h3>
                    {"<p class='text-gray-600 mt-1'>" + desc + "</p>" if desc else ""}
                </div>
            </div>'''

    quote_html = ""
    if slide.extra.get("quote"):
        q = slide.extra["quote"]
        quote_html = f'''<div class="mt-10 relative accent-gradient rounded-lg p-6">
            <div class="absolute left-0 top-0 bottom-0 w-1 rounded-l-lg" style="background:linear-gradient(to bottom,#4F46E5,#9333EA);"></div>
            <div class="flex items-start ml-4">
                <i class="ri-double-quotes-l text-indigo-500 text-2xl mr-2 flex-shrink-0"></i>
                <p class="text-lg text-gray-700 italic">{q}</p>
            </div>
        </div>'''

    return f'''<!-- Slide {n}: Table of Contents -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="flex justify-between items-center mb-10">
            <div>
                <h1 class="text-4xl font-bold text-gray-800">{title}</h1>
                <div class="accent-line mt-3"></div>
            </div>
            <span class="text-gray-500 text-lg font-medium">{subtitle}</span>
        </div>

        <div class="grid grid-cols-2 gap-6 mt-4">
            {items_html}
        </div>

        {quote_html}
    </div>

{slide_footer(n, config)}
</div>
'''
