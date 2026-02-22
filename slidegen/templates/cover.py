"""
Cover slide template - for title/intro and closing slides.
"""
from .base import slide_footer


def render_cover(slide, config=None):
    """Render a cover/title slide."""
    n = slide.slide_number
    title = slide.title
    subtitle = slide.subtitle or ""
    description = slide.description or ""
    icon = slide.icon or "ri-presentation-line"

    # Optional icon list from items
    icons_html = ""
    if slide.items:
        icon_items = []
        for item in slide.items:
            ic = item.icon if hasattr(item, 'icon') and item.icon else "ri-star-line"
            label = item.title if hasattr(item, 'title') else str(item)
            icon_items.append(f'''<div class="flex flex-col items-center">
                    <div class="w-14 h-14 rounded-2xl bg-indigo-50 flex items-center justify-center mb-2">
                        <i class="{ic} text-2xl text-indigo-600"></i>
                    </div>
                    <span class="text-xs text-gray-500">{label}</span>
                </div>''')
        icons_html = f'''<div class="flex items-center justify-center space-x-8 mt-8">
            {''.join(icon_items)}
        </div>'''

    extra_text = ""
    if slide.extra.get("cta"):
        extra_text = f'''<div class="mt-8">
            <h3 class="gradient-text text-2xl font-bold">{slide.extra["cta"]}</h3>
        </div>'''

    return f'''<!-- Slide {n}: Cover -->
<div class="slide-container px-16 py-12 flex flex-col justify-center items-center text-center">
    <div class="decoration-element" style="width:400px;height:400px;top:-100px;right:-100px;background:rgba(99,102,241,0.15);"></div>
    <div class="decoration-element" style="width:300px;height:300px;bottom:-80px;left:-80px;background:rgba(168,85,247,0.12);"></div>

    <div class="slide-content-wrapper flex flex-col justify-center items-center relative z-10">
        <div class="w-16 h-16 rounded-2xl bg-indigo-50 flex items-center justify-center mb-6">
            <i class="{icon} text-3xl text-indigo-600"></i>
        </div>
        <h1 class="text-6xl font-bold tracking-tight gradient-text leading-tight">{title}</h1>
        {"<h2 class='text-4xl font-semibold text-gray-800 mt-4'>" + subtitle + "</h2>" if subtitle else ""}
        {"<p class='text-lg text-gray-600 mt-4 max-w-2xl'>" + description + "</p>" if description else ""}

        <div class="border-t border-gray-200 w-1/3 my-6"></div>

        {icons_html}
        {extra_text}
    </div>

{slide_footer(n, config)}
</div>
'''
