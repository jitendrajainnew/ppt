"""
Table slide template - for structured data display.
"""
from .base import slide_footer


def render_table(slide, config=None):
    """Render a table slide."""
    n = slide.slide_number
    title = slide.title
    description = slide.description or ""

    headers = slide.extra.get("headers", [])
    rows = slide.extra.get("rows", [])

    # Build table header
    th_html = ""
    for h in headers:
        th_html += f'<th class="px-4 py-3 text-left text-sm font-semibold text-gray-700">{h}</th>'

    # Build table rows
    tr_html = ""
    for i, row in enumerate(rows):
        bg = "bg-gray-50" if i % 2 == 0 else "bg-white"
        td_html = ""
        for j, cell in enumerate(row):
            weight = "font-medium" if j == 0 else ""
            td_html += f'<td class="px-4 py-3 text-sm text-gray-700 {weight}">{cell}</td>'
        tr_html += f'<tr class="{bg}">{td_html}</tr>'

    # Optional insight
    insight_html = ""
    if slide.extra.get("insight"):
        insight_html = f'''<div class="mt-5 gradient-bg rounded-xl p-4 flex items-start space-x-3">
            <i class="ri-lightbulb-line text-lg text-indigo-500 mt-0.5 flex-shrink-0"></i>
            <p class="text-sm text-gray-700">{slide.extra["insight"]}</p>
        </div>'''

    return f'''<!-- Slide {n}: Table -->
<div class="slide-container px-16 py-12">
    <div class="slide-content-wrapper">
        <div class="mb-6">
            <h1 class="text-3xl font-bold text-gray-800">{title}</h1>
            <div class="accent-line mt-3"></div>
            {"<p class='text-gray-600 mt-3 max-w-3xl'>" + description + "</p>" if description else ""}
        </div>

        <div class="border border-gray-100 rounded-xl overflow-hidden">
            <table class="w-full">
                <thead class="bg-gray-50 border-b border-gray-100">
                    <tr>{th_html}</tr>
                </thead>
                <tbody class="divide-y divide-gray-50">
                    {tr_html}
                </tbody>
            </table>
        </div>

        {insight_html}
    </div>

{slide_footer(n, config)}
</div>
'''
