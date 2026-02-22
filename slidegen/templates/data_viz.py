"""
Data visualization slide - stats, metrics, charts.
"""
from .base import slide_footer


def render_data_viz(slide, config=None):
    """Render a data/stats visualization slide."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""

    color_sets = [
        {"bg": "bg-blue-50", "border": "border-blue-100", "text": "text-blue-600",
         "value": "text-blue-700", "bar": "bg-blue-500"},
        {"bg": "bg-purple-50", "border": "border-purple-100", "text": "text-purple-600",
         "value": "text-purple-700", "bar": "bg-purple-500"},
        {"bg": "bg-green-50", "border": "border-green-100", "text": "text-green-600",
         "value": "text-green-700", "bar": "bg-green-500"},
        {"bg": "bg-indigo-50", "border": "border-indigo-100", "text": "text-indigo-600",
         "value": "text-indigo-700", "bar": "bg-indigo-500"},
        {"bg": "bg-pink-50", "border": "border-pink-100", "text": "text-pink-600",
         "value": "text-pink-700", "bar": "bg-pink-500"},
        {"bg": "bg-orange-50", "border": "border-orange-100", "text": "text-orange-600",
         "value": "text-orange-700", "bar": "bg-orange-500"},
    ]

    # Stat cards
    stats_html = ""
    if slide.items:
        stat_items = ""
        for i, item in enumerate(slide.items):
            cs = color_sets[i % len(color_sets)]
            val = item.value if hasattr(item, 'value') else item.title if hasattr(item, 'title') else str(item)
            label = item.label if hasattr(item, 'label') else item.description if hasattr(item, 'description') else ""
            icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-bar-chart-line"

            stat_items += f'''<div class="stat-card {cs['bg']} border {cs['border']} rounded-xl p-5 text-center">
                    <div class="w-12 h-12 rounded-full {cs['bg']} flex items-center justify-center mx-auto mb-3">
                        <i class="{icon} text-2xl {cs['text']}"></i>
                    </div>
                    <div class="text-3xl font-bold {cs['value']}">{val}</div>
                    <div class="text-sm text-gray-600 mt-1">{label}</div>
                </div>'''

        cols = min(len(slide.items), 4)
        stats_html = f'''<div class="grid grid-cols-{cols} gap-5 mb-6">
            {stat_items}
        </div>'''

    # Optional bar chart / progress bars
    bars_html = ""
    if slide.extra.get("bars"):
        bar_items = ""
        for i, bar in enumerate(slide.extra["bars"]):
            cs = color_sets[i % len(color_sets)]
            label = bar.get("label", "")
            value = bar.get("value", 0)
            display = bar.get("display", f"{value}%")
            pct = min(int(value), 100) if isinstance(value, (int, float)) else 50
            bar_items += f'''<div class="mb-3">
                    <div class="flex justify-between text-sm mb-1">
                        <span class="text-gray-700 font-medium">{label}</span>
                        <span class="font-semibold {cs['value']}">{display}</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-bar-fill {cs['bar']}" style="width:{pct}%"></div>
                    </div>
                </div>'''
        bars_html = f'''<div class="bg-gray-50 rounded-xl p-6">
            {bar_items}
        </div>'''

    # Optional insight box
    insight_html = ""
    if slide.extra.get("insight"):
        insight_html = f'''<div class="mt-5 gradient-bg rounded-xl p-5 flex items-start space-x-3">
            <i class="ri-lightbulb-line text-xl text-indigo-500 mt-0.5 flex-shrink-0"></i>
            <div>
                <h4 class="text-sm font-semibold text-gray-800">Key Insight</h4>
                <p class="text-sm text-gray-600 mt-1">{slide.extra["insight"]}</p>
            </div>
        </div>'''

    return f'''<!-- Slide {n}: Data Visualization -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        {stats_html}
        {bars_html}
        {insight_html}
    </div>

{slide_footer(n, config)}
</div>
'''
