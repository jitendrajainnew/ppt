"""
SlideGen configuration - colors, fonts, layout settings.
"""


class SlideConfig:
    """Configuration for slide generation."""

    def __init__(self, **kwargs):
        # Layout
        self.slide_width = kwargs.get("slide_width", 1280)
        self.slide_min_height = kwargs.get("slide_min_height", 720)
        self.batch_size = kwargs.get("batch_size", 50)

        # Footer
        self.footer_author = kwargs.get("footer_author", "Jitendra Jain")
        self.footer_link = kwargs.get("footer_link", "https://x.com/jitendrajain")
        self.footer_icon = kwargs.get("footer_icon", "ri-twitter-x-line")

        # Colors
        self.gradient_start = kwargs.get("gradient_start", "#0066FF")
        self.gradient_mid = kwargs.get("gradient_mid", "#5933EA")
        self.gradient_end = kwargs.get("gradient_end", "#AF33D9")

        # Accent color palettes for cards/sections
        self.accent_colors = kwargs.get("accent_colors", [
            {"name": "blue", "bg": "bg-blue-50", "border": "border-blue-100",
             "text": "text-blue-700", "icon": "text-blue-600", "fill": "bg-blue-500"},
            {"name": "purple", "bg": "bg-purple-50", "border": "border-purple-100",
             "text": "text-purple-700", "icon": "text-purple-600", "fill": "bg-purple-500"},
            {"name": "green", "bg": "bg-green-50", "border": "border-green-100",
             "text": "text-green-700", "icon": "text-green-600", "fill": "bg-green-500"},
            {"name": "indigo", "bg": "bg-indigo-50", "border": "border-indigo-100",
             "text": "text-indigo-700", "icon": "text-indigo-600", "fill": "bg-indigo-500"},
            {"name": "pink", "bg": "bg-pink-50", "border": "border-pink-100",
             "text": "text-pink-700", "icon": "text-pink-600", "fill": "bg-pink-500"},
            {"name": "orange", "bg": "bg-orange-50", "border": "border-orange-100",
             "text": "text-orange-700", "icon": "text-orange-600", "fill": "bg-orange-500"},
            {"name": "red", "bg": "bg-red-50", "border": "border-red-100",
             "text": "text-red-700", "icon": "text-red-600", "fill": "bg-red-500"},
            {"name": "teal", "bg": "bg-teal-50", "border": "border-teal-100",
             "text": "text-teal-700", "icon": "text-teal-600", "fill": "bg-teal-500"},
        ])

    def get_accent(self, index):
        """Get accent color by index, cycling through available colors."""
        return self.accent_colors[index % len(self.accent_colors)]

    def gradient_css(self):
        """Return the main gradient CSS string."""
        return f"linear-gradient(90deg, {self.gradient_start} 0%, {self.gradient_mid} 50%, {self.gradient_end} 100%)"
