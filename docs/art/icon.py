"""Render the GUIDE plugin icon (the three-alignments mark) as a square PNG.

Same geometry and colors as the mark in hero.html: a triangle with
effective (blue) at the top, efficient (green) at bottom left, and
engaging (amber) at bottom right. Drawn at 4x and downsampled for
smooth edges.

Usage: python docs/art/icon.py
Writes skill/guide-instructional-design-plugin/.claude-plugin/icon.png
"""

from pathlib import Path

from PIL import Image, ImageDraw

SIZE = 1024
SS = 4  # supersampling factor
BG = "#0f172a"
STROKE = "#bfdbfe"
BLUE, GREEN, AMBER = "#2563eb", "#059669", "#d97706"

# Mark geometry from hero.html (viewBox 0 0 84 76).
TOP, LEFT, RIGHT = (42, 8), (8, 68), (76, 68)
DOT_R, STROKE_W = 7.5, 3
MARK_CENTER = (42, 38)
SCALE = 7.6  # mark units to output pixels; the mark fills about 60% of the icon

OUT = (
    Path(__file__).resolve().parents[2]
    / "skill" / "guide-instructional-design-plugin" / ".claude-plugin" / "icon.png"
)


def to_px(pt):
    s = SCALE * SS
    c = SIZE * SS / 2
    return (c + (pt[0] - MARK_CENTER[0]) * s, c + (pt[1] - MARK_CENTER[1]) * s)


def main() -> None:
    big = SIZE * SS
    img = Image.new("RGB", (big, big), BG)
    draw = ImageDraw.Draw(img)

    corners = [to_px(p) for p in (TOP, RIGHT, LEFT)]
    width = round(STROKE_W * SCALE * SS)
    draw.line(corners + [corners[0]], fill=STROKE, width=width, joint="curve")
    # Round the joins the way stroke-linejoin="round" does.
    for x, y in corners:
        draw.ellipse((x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=STROKE)

    r = DOT_R * SCALE * SS
    for pt, color in ((TOP, BLUE), (LEFT, GREEN), (RIGHT, AMBER)):
        x, y = to_px(pt)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)

    img.resize((SIZE, SIZE), Image.LANCZOS).save(OUT, optimize=True)
    print(f"Wrote {OUT} ({SIZE}x{SIZE}).")


if __name__ == "__main__":
    main()
