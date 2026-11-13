#!/usr/bin/env python3
"""Rasterize assets/*.svg to PNG at 2x for the printable rubric.

The README shows the SVGs directly. Word cannot be relied on to render SVG, so
docs/build_rubric_docx.py embeds the PNGs this script writes. It drives a
Chromium-based browser (Edge or Chrome) in headless mode, so the PNGs match what
a browser shows for the SVG. All diagrams are drawn in code and are Apache-2.0
like the rest of the repository.

Run from the repo root after editing an SVG:
    python docs/art/render_diagrams.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS = REPO_ROOT / "assets"
SCALE = 2
CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def find_browser() -> str:
    for name in ("msedge", "chrome", "google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return found
    for path in CANDIDATES:
        if Path(path).exists():
            return path
    raise SystemExit("No Edge or Chrome found. Install one, or rasterize the SVGs another way.")


def render(browser: str, svg: Path) -> Path:
    text = svg.read_text(encoding="utf-8")
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', text)
    if not m:
        raise SystemExit(f"{svg.name}: no viewBox")
    width, height = m.group(1), m.group(2)
    png = svg.with_suffix(".png")
    # Work in a local temp folder: the browser can return before the file lands, and
    # may not be allowed to read or write the repository's drive.
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as work:
        work_dir = Path(work)
        local_svg = work_dir / svg.name
        local_png = work_dir / png.name
        shutil.copyfile(svg, local_svg)
        subprocess.run(
            [
                browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                f"--force-device-scale-factor={SCALE}", f"--window-size={width},{height}",
                f"--user-data-dir={work_dir / 'profile'}", f"--screenshot={local_png}", local_svg.as_uri(),
            ],
            check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
        )
        deadline = time.time() + 60
        while time.time() < deadline and not (local_png.exists() and local_png.stat().st_size > 0):
            time.sleep(0.5)
        if not local_png.exists():
            raise SystemExit(f"{svg.name}: the browser wrote no PNG")
        time.sleep(0.5)
        shutil.copyfile(local_png, png)
    return png


def main() -> int:
    browser = find_browser()
    svgs = sorted(ASSETS.glob("*.svg"))
    for svg in svgs:
        png = render(browser, svg)
        print(f"  {svg.name} -> {png.name}")
    print(f"Rendered {len(svgs)} diagram(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
