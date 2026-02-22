"""
Section break slide - transition between major sections.
"""
from .base import slide_footer


def render_section_break(slide, config=None):
    """Render a section divider slide."""
    n = slide.slide_number
    title = slide.title
    subtitle = slide.subtitle or ""
    description = slide.description or ""
    icon = slide.icon or "ri-bookmark-line"
    section_num = slide.extra.get("section_number", "")

    return f'''<!-- Slide {n}: Section Break -->
<div class="slide-container px-16 py-12 flex flex-col justify-center items-center text-center">
    <div class="decoration-element" style="width:350px;height:350px;top:-80px;left:-80px;background:rgba(99,102,241,0.12);"></div>
    <div class="decoration-element" style="width:250px;height:250px;bottom:-60px;right:-60px;background:rgba(168,85,247,0.10);"></div>

    <div class="slide-content-wrapper flex flex-col justify-center items-center relative z-10">
        {"<span class='text-sm font-medium text-indigo-500 tracking-widest uppercase mb-4'>Section " + str(section_num) + "</span>" if section_num else ""}
        <div class="w-16 h-16 rounded-2xl bg-indigo-50 flex items-center justify-center mb-6">
            <i class="{icon} text-3xl text-indigo-600"></i>
        </div>
        <h1 class="text-5xl font-bold gradient-text leading-tight">{title}</h1>
        {"<h2 class='text-2xl font-medium text-gray-600 mt-4'>" + subtitle + "</h2>" if subtitle else ""}
        <div class="accent-line mt-6 mx-auto"></div>
        {"<p class='text-gray-500 mt-6 max-w-xl text-lg'>" + description + "</p>" if description else ""}
    </div>

{slide_footer(n, config)}
</div>
'''
