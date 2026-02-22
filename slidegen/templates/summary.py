"""
Summary/conclusion slide template.
"""
from .base import slide_footer


def render_summary(slide, config=None):
    """Render a summary/key-takeaways slide."""
    n = slide.slide_number
    title = slide.title or "Key Takeaways"
    description = slide.description or ""

    color_sets = [
        {"bg": "bg-blue-50", "icon": "text-blue-600", "border": "border-blue-100"},
        {"bg": "bg-purple-50", "icon": "text-purple-600", "border": "border-purple-100"},
        {"bg": "bg-green-50", "icon": "text-green-600", "border": "border-green-100"},
        {"bg": "bg-indigo-50", "icon": "text-indigo-600", "border": "border-indigo-100"},
        {"bg": "bg-pink-50", "icon": "text-pink-600", "border": "border-pink-100"},
        {"bg": "bg-orange-50", "icon": "text-orange-600", "border": "border-orange-100"},
    ]

    # Key points (left column)
    points_html = ""
    for i, item in enumerate(slide.items):
        cs = color_sets[i % len(color_sets)]
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') and item.description else ""
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-check-double-line"

        points_html += f'''<div class="card flex items-start space-x-4 p-4 rounded-xl border border-gray-100">
                <div class="w-10 h-10 rounded-lg {cs['bg']} flex items-center justify-center flex-shrink-0">
                    <i class="{icon} text-xl {cs['icon']}"></i>
                </div>
                <div>
                    <h3 class="text-base font-semibold text-gray-800">{t}</h3>
                    {"<p class='text-sm text-gray-600 mt-1'>" + desc + "</p>" if desc else ""}
                </div>
            </div>'''

    # Future outlook / right sidebar
    outlook_html = ""
    if slide.extra.get("outlook"):
        outlook_items = ""
        for oi in slide.extra["outlook"]:
            icon = oi.get("icon", "ri-arrow-right-s-line")
            text = oi.get("text", "")
            outlook_items += f'''<div class="flex items-start space-x-2 mb-2">
                    <i class="{icon} text-indigo-500 mt-0.5 flex-shrink-0"></i>
                    <span class="text-sm text-gray-700">{text}</span>
                </div>'''
        outlook_html = f'''<div class="gradient-bg rounded-xl p-5">
                <h3 class="text-base font-semibold text-gray-800 mb-3">
                    <i class="ri-rocket-line text-indigo-500 mr-2"></i>
                    {slide.extra.get("outlook_title", "Looking Ahead")}
                </h3>
                {outlook_items}
            </div>'''

    # References
    refs_html = ""
    if slide.extra.get("references"):
        ref_items = ""
        for ref in slide.extra["references"]:
            ref_items += f'''<div class="flex items-center space-x-2 mb-2">
                    <i class="ri-link text-gray-400 flex-shrink-0"></i>
                    <span class="text-sm text-gray-600">{ref}</span>
                </div>'''
        refs_html = f'''<div class="bg-white rounded-xl border border-gray-100 p-5 mt-4">
                <h3 class="text-base font-semibold text-gray-800 mb-3">References</h3>
                {ref_items}
            </div>'''

    has_sidebar = outlook_html or refs_html

    if has_sidebar:
        return f'''<!-- Slide {n}: Summary -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid grid-cols-3 gap-6">
            <div class="col-span-2 space-y-3">
                {points_html}
            </div>
            <div class="space-y-4">
                {outlook_html}
                {refs_html}
            </div>
        </div>
    </div>

{slide_footer(n, config)}
</div>
'''
    else:
        return f'''<!-- Slide {n}: Summary -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid grid-cols-2 gap-4">
            {points_html}
        </div>
    </div>

{slide_footer(n, config)}
</div>
'''
