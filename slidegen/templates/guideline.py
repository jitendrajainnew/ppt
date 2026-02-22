"""
Guideline/Strategy slide template - step-by-step strategies, case studies.
"""
from .base import slide_footer


def render_guideline(slide, config=None):
    """Render a guideline/strategy slide."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""
    cols = slide.columns or 2

    color_sets = [
        {"bg": "bg-blue-50", "border": "border-blue-100", "text": "text-blue-700",
         "icon": "text-blue-600", "num_bg": "bg-blue-500"},
        {"bg": "bg-purple-50", "border": "border-purple-100", "text": "text-purple-700",
         "icon": "text-purple-600", "num_bg": "bg-purple-500"},
        {"bg": "bg-green-50", "border": "border-green-100", "text": "text-green-700",
         "icon": "text-green-600", "num_bg": "bg-green-500"},
        {"bg": "bg-indigo-50", "border": "border-indigo-100", "text": "text-indigo-700",
         "icon": "text-indigo-600", "num_bg": "bg-indigo-500"},
    ]

    items_html = ""
    for i, item in enumerate(slide.items):
        cs = color_sets[i % len(color_sets)]
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') and item.description else ""
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-guide-line"

        points_html = ""
        pts = item.points if hasattr(item, 'points') else []
        for pt in pts:
            points_html += f'''<li class="flex items-start space-x-2 mb-1.5">
                        <i class="ri-checkbox-circle-line {cs['icon']} mt-0.5 flex-shrink-0 text-sm"></i>
                        <span class="text-gray-700 text-sm">{pt}</span>
                    </li>'''

        extra_note = ""
        if hasattr(item, 'extra') and item.extra.get("note"):
            extra_note = f'<div class="mt-3 p-2 {cs["bg"]} rounded text-xs {cs["text"]}"><i class="ri-lightbulb-line mr-1"></i>{item.extra["note"]}</div>'

        items_html += f'''<div class="border border-gray-100 rounded-xl overflow-hidden card">
                <div class="{cs['bg']} px-5 py-3 flex items-center space-x-3 border-b {cs['border']}">
                    <div class="w-8 h-8 rounded-lg {cs['num_bg']} text-white flex items-center justify-center text-sm font-bold">{i+1}</div>
                    <div class="flex items-center space-x-2">
                        <i class="{icon} {cs['icon']}"></i>
                        <h3 class="text-base font-semibold text-gray-800">{t}</h3>
                    </div>
                </div>
                <div class="p-5">
                    {"<p class='text-sm text-gray-600 mb-2'>" + desc + "</p>" if desc else ""}
                    <ul>{points_html}</ul>
                    {extra_note}
                </div>
            </div>'''

    # Best practices box
    best_html = ""
    if slide.extra.get("best_practices"):
        bp_items = ""
        for bp in slide.extra["best_practices"]:
            bp_items += f'''<div class="flex items-start space-x-2">
                    <i class="ri-star-line text-yellow-500 mt-0.5 flex-shrink-0"></i>
                    <span class="text-sm text-gray-700">{bp}</span>
                </div>'''
        best_html = f'''<div class="mt-5 bg-yellow-50 border border-yellow-100 rounded-xl p-5">
            <h4 class="text-sm font-semibold text-yellow-800 mb-3"><i class="ri-award-line mr-1"></i>Best Practices</h4>
            <div class="grid grid-cols-2 gap-2">{bp_items}</div>
        </div>'''

    grid_class = f"grid-cols-{min(cols, 3)}"

    return f'''<!-- Slide {n}: Guideline -->
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

        {best_html}
    </div>

{slide_footer(n, config)}
</div>
'''
