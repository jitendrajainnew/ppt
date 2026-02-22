"""
Two-column content slide template - text + sidebar or split layout.
"""
from .base import slide_footer


def render_two_column(slide, config=None):
    """Render a two-column content slide."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""

    # Left column items (main content)
    left_html = ""
    for i, item in enumerate(slide.items):
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') and item.description else ""
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-arrow-right-s-line"

        points_html = ""
        pts = item.points if hasattr(item, 'points') else []
        for pt in pts:
            points_html += f'''<li class="flex items-start space-x-2 mb-1.5">
                        <i class="ri-check-line text-green-500 mt-0.5 flex-shrink-0 text-sm"></i>
                        <span class="text-gray-700 text-sm">{pt}</span>
                    </li>'''

        left_html += f'''<div class="mb-4">
                <div class="flex items-center space-x-2 mb-2">
                    <i class="{icon} text-indigo-500"></i>
                    <h3 class="text-lg font-semibold text-gray-800">{t}</h3>
                </div>
                {"<p class='text-gray-600 text-sm mb-2'>" + desc + "</p>" if desc else ""}
                {"<ul>" + points_html + "</ul>" if points_html else ""}
            </div>'''

    # Right column (sidebar content from extra)
    right_html = ""
    if slide.extra.get("sidebar_items"):
        sidebar_items = ""
        for si in slide.extra["sidebar_items"]:
            si_title = si.get("title", "")
            si_desc = si.get("description", "")
            si_icon = si.get("icon", "ri-information-line")
            sidebar_items += f'''<div class="p-4 bg-white rounded-lg border border-gray-100 card mb-3">
                    <div class="flex items-center space-x-2 mb-2">
                        <i class="{si_icon} text-indigo-500"></i>
                        <h4 class="text-sm font-semibold text-gray-800">{si_title}</h4>
                    </div>
                    <p class="text-xs text-gray-600">{si_desc}</p>
                </div>'''
        right_html = f'''<div class="gradient-bg rounded-xl p-4">
            <h3 class="text-base font-semibold text-gray-800 mb-3">{slide.extra.get("sidebar_title", "Key Points")}</h3>
            {sidebar_items}
        </div>'''

    if slide.extra.get("sidebar_text"):
        right_html = f'''<div class="gradient-bg rounded-xl p-6">
            <h3 class="text-base font-semibold text-gray-800 mb-3">{slide.extra.get("sidebar_title", "Key Insight")}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{slide.extra["sidebar_text"]}</p>
        </div>'''

    return f'''<!-- Slide {n}: Two Column -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid grid-cols-3 gap-6">
            <div class="col-span-2">
                {left_html}
            </div>
            <div>
                {right_html}
            </div>
        </div>
    </div>

{slide_footer(n, config)}
</div>
'''
