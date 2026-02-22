"""
List/Feature slide template - multiple features/principles in card layout.
"""
from .base import slide_footer


def render_list_feature(slide, config=None):
    """Render a list/feature slide with cards in a grid."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""
    cols = slide.columns or 2

    color_sets = [
        {"bg": "bg-blue-50", "border": "border-blue-100", "text": "text-blue-700", "icon": "text-blue-600"},
        {"bg": "bg-purple-50", "border": "border-purple-100", "text": "text-purple-700", "icon": "text-purple-600"},
        {"bg": "bg-green-50", "border": "border-green-100", "text": "text-green-700", "icon": "text-green-600"},
        {"bg": "bg-indigo-50", "border": "border-indigo-100", "text": "text-indigo-700", "icon": "text-indigo-600"},
        {"bg": "bg-pink-50", "border": "border-pink-100", "text": "text-pink-700", "icon": "text-pink-600"},
        {"bg": "bg-orange-50", "border": "border-orange-100", "text": "text-orange-700", "icon": "text-orange-600"},
    ]

    items_html = ""
    for i, item in enumerate(slide.items):
        cs = color_sets[i % len(color_sets)]
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') and item.description else ""
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-checkbox-circle-line"
        badge = item.badge if hasattr(item, 'badge') and item.badge else ""

        points_html = ""
        pts = item.points if hasattr(item, 'points') else []
        for pt in pts:
            points_html += f'''<li class="flex items-start space-x-2 mb-1.5">
                        <i class="ri-check-line {cs['icon']} mt-0.5 flex-shrink-0 text-sm"></i>
                        <span class="text-gray-700 text-sm">{pt}</span>
                    </li>'''

        badge_html = f'<span class="text-xs {cs["bg"]} {cs["text"]} px-2 py-0.5 rounded-full border {cs["border"]} ml-2">{badge}</span>' if badge else ""

        extra_box = ""
        if hasattr(item, 'extra') and item.extra.get("note"):
            extra_box = f'<div class="mt-3 p-2 {cs["bg"]} rounded text-xs {cs["text"]}">{item.extra["note"]}</div>'

        items_html += f'''<div class="border border-gray-100 rounded-xl p-5 card">
                <div class="flex items-center mb-3">
                    <div class="w-10 h-10 rounded-lg {cs['bg']} flex items-center justify-center flex-shrink-0">
                        <i class="{icon} text-xl {cs['icon']}"></i>
                    </div>
                    <h3 class="text-base font-semibold text-gray-800 ml-3">{t}</h3>
                    {badge_html}
                </div>
                {"<p class='text-gray-600 text-sm mb-2'>" + desc + "</p>" if desc else ""}
                <ul>
                    {points_html}
                </ul>
                {extra_box}
            </div>'''

    # Optional bottom section
    bottom_html = ""
    if slide.extra.get("bottom_title"):
        bottom_items = slide.extra.get("bottom_items", [])
        bi_html = ""
        for bi in bottom_items:
            bi_html += f'''<div class="text-center p-3 bg-white rounded-lg border border-gray-100">
                    <div class="text-sm font-medium text-gray-800">{bi.get("title", "")}</div>
                    <div class="text-xs text-gray-500 mt-1">{bi.get("desc", "")}</div>
                </div>'''
        bottom_html = f'''<div class="mt-6 gradient-bg rounded-xl p-5">
            <h4 class="text-sm font-semibold text-gray-700 mb-3">{slide.extra["bottom_title"]}</h4>
            <div class="grid grid-cols-{min(len(bottom_items), 4)} gap-3">
                {bi_html}
            </div>
        </div>'''

    grid_class = f"grid-cols-{min(cols, 3)}"

    return f'''<!-- Slide {n}: Features -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid {grid_class} gap-5">
            {items_html}
        </div>

        {bottom_html}
    </div>

{slide_footer(n, config)}
</div>
'''
