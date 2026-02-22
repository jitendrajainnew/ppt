"""
CLI entry point for SlideGen.

Usage:
    python -m slidegen generate <script.py> [--output-dir DIR] [--title TITLE]
    python -m slidegen demo [--output-dir DIR]

The generate command imports and runs a slide script that defines slides.
The demo command generates a sample presentation.
"""
import argparse
import importlib.util
import os
import sys

from .config import SlideConfig
from .generator import generate_html, generate_single_html


def main():
    parser = argparse.ArgumentParser(
        description="SlideGen - HTML Slide Deck Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m slidegen demo
  python -m slidegen demo --output-dir ./my_slides
  python -m slidegen generate my_deck.py --title "My Presentation"
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Demo command
    demo_parser = subparsers.add_parser("demo", help="Generate a demo presentation")
    demo_parser.add_argument("--output-dir", "-o", default="./slidegen/output",
                             help="Output directory (default: ./slidegen/output)")
    demo_parser.add_argument("--single", action="store_true",
                             help="Generate a single HTML file (no batching)")

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate slides from a script")
    gen_parser.add_argument("script", help="Python script defining slides")
    gen_parser.add_argument("--output-dir", "-o", default="./slidegen/output",
                            help="Output directory (default: ./slidegen/output)")
    gen_parser.add_argument("--title", "-t", default="Presentation",
                            help="Presentation title")
    gen_parser.add_argument("--single", action="store_true",
                            help="Generate a single HTML file (no batching)")
    gen_parser.add_argument("--author", default="Jitendra Jain",
                            help="Footer author name")
    gen_parser.add_argument("--author-link", default="https://x.com/jitendrajain",
                            help="Footer author link")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    if args.command == "demo":
        _run_demo(args)
    elif args.command == "generate":
        _run_generate(args)


def _run_demo(args):
    """Run the demo presentation generator."""
    from .examples.demo_deck import build_demo_slides
    slides = build_demo_slides()
    config = SlideConfig()

    print(f"SlideGen Demo: Generating {len(slides)} slides...")

    if args.single:
        html = generate_single_html(slides, "SlideGen Demo", config)
        os.makedirs(args.output_dir, exist_ok=True)
        path = os.path.join(args.output_dir, "demo_slides.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Written: {path}")
    else:
        generate_html(slides, "SlideGen Demo", config, args.output_dir)

    print("Done!")


def _run_generate(args):
    """Run a user-provided slide script."""
    script_path = os.path.abspath(args.script)
    if not os.path.exists(script_path):
        print(f"Error: Script not found: {script_path}")
        sys.exit(1)

    # Load the script as a module
    spec = importlib.util.spec_from_file_location("slide_script", script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # The script must define build_slides() -> list of SlideContent
    if not hasattr(mod, "build_slides"):
        print("Error: Script must define a build_slides() function")
        print("  The function should return a list of SlideContent objects")
        sys.exit(1)

    slides = mod.build_slides()

    config = SlideConfig(
        footer_author=args.author,
        footer_link=args.author_link,
    )

    print(f"SlideGen: Generating {len(slides)} slides from {args.script}...")

    if args.single:
        html = generate_single_html(slides, args.title, config)
        os.makedirs(args.output_dir, exist_ok=True)
        slug = args.title.lower().replace(" ", "_")[:40]
        path = os.path.join(args.output_dir, f"{slug}_slides.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Written: {path}")
    else:
        generate_html(slides, args.title, config, args.output_dir)

    print("Done!")


if __name__ == "__main__":
    main()
