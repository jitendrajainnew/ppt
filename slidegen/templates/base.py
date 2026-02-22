"""
Base HTML template - head, styles, print CSS, and wrapper.
"""


def html_head(title="Presentation", config=None):
    """Generate the full HTML head and opening body tags."""
    gradient = "linear-gradient(90deg, #0066FF 0%, #5933EA 50%, #AF33D9 100%)"
    if config:
        gradient = config.gradient_css()

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        body {{ background-color: #f3f4f6; }}

        .slide-container {{
            width: 1280px;
            min-height: 720px;
            margin: 2rem auto;
            position: relative;
            overflow: hidden;
            background: white;
            display: flex;
            flex-direction: column;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}

        .slide-content-wrapper {{
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }}

        .footer {{
            margin-top: auto;
            padding: 1rem 4rem 1.5rem 4rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .footer a {{
            color: #9ca3af;
            text-decoration: none;
            font-size: 0.75rem;
            transition: color 0.2s;
        }}
        .footer a:hover {{ color: #6b7280; }}
        .footer-page-number {{
            font-size: 0.875rem;
            color: #9ca3af;
        }}

        .gradient-text {{
            background: {gradient};
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }}
        .accent-line {{
            height: 4px;
            width: 80px;
            border-radius: 2px;
            background: {gradient};
        }}
        .gradient-bg {{
            background: linear-gradient(135deg, rgba(79,70,229,0.05) 0%, rgba(147,51,234,0.05) 100%);
        }}
        .accent-gradient {{
            background: linear-gradient(135deg, rgba(79,70,229,0.15) 0%, rgba(147,51,234,0.07) 100%);
        }}

        .decoration-element {{
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            z-index: 0;
        }}

        .card {{
            transition: all 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }}

        .faq-q-icon::before {{
            content: "\\f15f";
            font-family: 'remixicon';
            font-size: 1.25rem;
            color: #3b82f6;
            margin-right: 0.75rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
            display: inline-block;
        }}
        .faq-a-icon::before {{
            content: "\\eaed";
            font-family: 'remixicon';
            font-size: 1.25rem;
            color: #10b981;
            margin-right: 0.75rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
            display: inline-block;
        }}

        .stat-card {{
            transition: all 0.3s ease;
        }}
        .stat-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        }}

        .progress-bar {{
            height: 8px;
            border-radius: 4px;
            background: #e5e7eb;
            overflow: hidden;
        }}
        .progress-bar-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.6s ease;
        }}

        .timeline-line {{
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, #818cf8, #a78bfa, #c084fc);
            transform: translateX(-50%);
        }}
        .timeline-dot {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            border: 2px solid white;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1;
        }}

        .quote-left-bar {{
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            border-radius: 2px;
            background: linear-gradient(to bottom, #4F46E5, #9333EA);
        }}

        /* Print button */
        .print-btn {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 9999;
            background: linear-gradient(135deg, #4F46E5, #7C3AED);
            color: white;
            border: none;
            border-radius: 50%;
            width: 56px;
            height: 56px;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(79,70,229,0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }}
        .print-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(79,70,229,0.5);
        }}

        /* Print styles */
        @media print {{
            @page {{
                size: auto;
                margin: 0mm;
            }}
            body {{
                padding: 0 !important;
                margin: 0 !important;
                background-color: white !important;
            }}
            .slide-container {{
                width: 100% !important;
                height: 100vh !important;
                min-height: 0 !important;
                margin: 0 !important;
                padding: 1.5rem 2rem !important;
                box-shadow: none !important;
                border-radius: 0 !important;
                page-break-after: always !important;
                overflow: hidden !important;
            }}
            .slide-container:last-child {{
                page-break-after: auto !important;
            }}
            .decoration-element, .no-print {{
                display: none !important;
            }}
            * {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            .footer {{
                padding: 0.5rem 2rem !important;
            }}
        }}
    </style>
</head>
<body>
    <button class="print-btn no-print" onclick="window.print()" title="Print / Save as PDF">
        <i class="ri-printer-line"></i>
    </button>
'''


def html_foot():
    """Generate the closing body and html tags."""
    return '''
<!-- PLACEHOLDER FOR NEXT SLIDES -->
</body>
</html>'''


def slide_footer(slide_number, config=None):
    """Generate footer HTML for a slide."""
    author = "Jitendra Jain"
    link = "https://x.com/jitendrajain"
    icon = "ri-twitter-x-line"
    if config:
        author = config.footer_author
        link = config.footer_link
        icon = config.footer_icon

    return f'''    <div class="footer">
        <div class="footer-source">
            <a href="{link}" target="_blank" class="flex items-center space-x-2">
                <i class="{icon}"></i>
                <span>Made by {author}</span>
            </a>
        </div>
        <div class="footer-page-number">{slide_number}</div>
    </div>'''
