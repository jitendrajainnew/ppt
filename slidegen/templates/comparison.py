"""
Comparison slide template - side-by-side comparisons.
"""
from .base import slide_footer


def render_comparison(slide, config=None):
    """Render a comparison slide with 2-3 columns."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""
    cols = min(slide.columns or 2, 3)

    color_sets = [
        {"bg": "bg-blue-50", "border": "border-blue-100", "text": "text-blue-700",
         "icon": "text-blue-600", "fill": "bg-blue-500", "bar": "bg-blue-500"},
        {"bg": "bg-purple-50", "border": "border-purple-100", "text": "text-purple-700",
         "icon": "text-purple-600", "fill": "bg-purple-500", "bar": "bg-purple-500"},
        {"bg": "bg-green-50", "border": "border-green-100", "text": "text-green-700",
         "icon": "text-green-600", "fill": "bg-green-500", "bar": "bg-green-500"},
    ]

    items_html = ""
    for i, item in enumerate(slide.items[:cols]):
        cs = color_sets[i % len(color_sets)]
        t = item.title if hasattr(item, 'title') else str(item)
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-star-line"
        badge = item.badge if hasattr(item, 'badge') and item.badge else ""

        points_html = ""
        pts = item.points if hasattr(item, 'points') else []
        for pt in pts:
            points_html += f'''<li class="flex items-start space-x-2 mb-2">
                        <i class="ri-check-line {cs['icon']} mt-0.5 flex-shrink-0"></i>
                        <span class="text-gray-700 text-sm">{pt}</span>
                    </li>'''

        metrics_html = ""
        metrics = item.metrics if hasattr(item, 'metrics') and item.metrics else {}
        for label, value in metrics.items():
            pct = 75
            if isinstance(value, (int, float)):
                pct = min(int(value), 100)
                value = f"{value}%"
            metrics_html += f'''<div class="mt-2">
                        <div class="flex justify-between text-xs text-gray-600 mb-1">
                            <span>{label}</span><span class="font-medium">{value}</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-bar-fill {cs['bar']}" style="width:{pct}%"></div>
                        </div>
                    </div>'''

        badge_html = f'<span class="text-xs {cs["bg"]} {cs["text"]} px-2 py-0.5 rounded-full border {cs["border"]}">{badge}</span>' if badge else ""

        items_html += f'''<div class="border border-gray-100 rounded-2xl overflow-hidden card">
                <div class="{cs['bg']} {cs['border']} border-b px-5 py-4 flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full {cs['bg']} flex items-center justify-center">
                            <i class="{icon} text-xl {cs['icon']}"></i>
                        </div>
                        <h3 class="text-lg font-semibold text-gray-800">{t}</h3>
                    </div>
                    {badge_html}
                </div>
                <div class="p-5">
                    <ul class="space-y-1">
                        {points_html}
                    </ul>
                    {metrics_html}
                </div>
            </div>'''

    # Bottom summary row
    summary_html = ""
    if slide.extra.get("summary_items"):
        summary_items_html = ""
        for si in slide.extra["summary_items"]:
            label = si.get("label", "")
            values = si.get("values", [])
            vals_html = "".join(f'<span class="text-sm text-gray-700">{v}</span>' for v in values)
            summary_items_html += f'''<div class="text-center">
                    <div class="text-xs text-gray-500 font-medium mb-1">{label}</div>
                    <div class="flex flex-col space-y-1">{vals_html}</div>
                </div>'''
        summary_html = f'''<div class="mt-6 gradient-bg rounded-xl p-5 grid grid-cols-{len(slide.extra['summary_items'])} gap-4">
            {summary_items_html}
        </div>'''

    grid_class = f"grid-cols-{cols}"

    return f'''<!-- Slide {n}: Comparison -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid {grid_class} gap-6">
            {items_html}
        </div>

        {summary_html}
    </div>

{slide_footer(n, config)}
</div>
'''
