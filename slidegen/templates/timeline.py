"""
Timeline slide template.
"""
from .base import slide_footer


def render_timeline(slide, config=None):
    """Render a timeline/process slide."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""

    color_fills = [
        "bg-blue-500", "bg-purple-500", "bg-green-500", "bg-indigo-500",
        "bg-pink-500", "bg-orange-500", "bg-teal-500"
    ]
    color_bgs = [
        "bg-blue-50", "bg-purple-50", "bg-green-50", "bg-indigo-50",
        "bg-pink-50", "bg-orange-50", "bg-teal-50"
    ]
    color_texts = [
        "text-blue-600", "text-purple-600", "text-green-600", "text-indigo-600",
        "text-pink-600", "text-orange-600", "text-teal-600"
    ]

    steps_html = ""
    for i, item in enumerate(slide.items):
        t = item.title if hasattr(item, 'title') else str(item)
        desc = item.description if hasattr(item, 'description') and item.description else ""
        label = item.label if hasattr(item, 'label') and item.label else f"Step {i+1}"
        icon = item.icon if hasattr(item, 'icon') and item.icon else "ri-arrow-right-circle-line"
        cf = color_fills[i % len(color_fills)]
        cb = color_bgs[i % len(color_bgs)]
        ct = color_texts[i % len(color_texts)]
        is_last = i == len(slide.items) - 1

        connector = "" if is_last else f'<div class="hidden md:block absolute top-1/2 -right-4 w-8 h-0.5 bg-gray-200"></div>'

        steps_html += f'''<div class="relative flex flex-col items-center text-center">
                <div class="w-14 h-14 rounded-2xl {cb} flex items-center justify-center mb-3">
                    <i class="{icon} text-2xl {ct}"></i>
                </div>
                <span class="text-xs font-medium {ct} px-2 py-0.5 rounded-full {cb} mb-2">{label}</span>
                <h3 class="text-sm font-semibold text-gray-800 mb-1">{t}</h3>
                {"<p class='text-xs text-gray-500'>" + desc + "</p>" if desc else ""}
                {connector}
            </div>'''

    cols = min(len(slide.items), 5)

    # Optional summary
    summary_html = ""
    if slide.extra.get("summary"):
        summary_html = f'''<div class="mt-6 gradient-bg rounded-xl p-5 flex items-start space-x-3">
            <i class="ri-information-line text-xl text-indigo-500 mt-0.5 flex-shrink-0"></i>
            <p class="text-sm text-gray-700">{slide.extra["summary"]}</p>
        </div>'''

    return f'''<!-- Slide {n}: Timeline -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        <div class="grid grid-cols-{cols} gap-6 relative">
            {steps_html}
        </div>

        {summary_html}
    </div>

{slide_footer(n, config)}
</div>
'''
