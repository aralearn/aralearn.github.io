#!/usr/bin/env python3
"""Makes the website's phone screens from the iPhone app's QA screenshots.

    python3 tools/make_shots.py <folder with the QA pictures>

The pictures come from the app repo's qa run (branch qa-screenshots, or the run's
"screenshots" artifact): <light|dark>-NN-<page>.png in English, polish-<page>.png and
polish-dark-<page>.png in Polish. Writes shots/<name>-<light|dark>.webp (English) and
shots/pl/<name>-<light|dark>.webp (Polish), 603 x 1311. A Polish screen that is missing
is skipped; the Polish page then falls back to the English one.

The Simulator's own Dynamic Island is painted out (filled with the colour just below it):
frame.webp draws its own, slightly narrower one.
"""
import glob
import math
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# website name -> the QA page name (after the light-NN- / polish- prefix)
PAGES = {
    "home": "home",
    "phrase": "phrase-pb-ak-gamicheret-tu-sheidzleba",
    "alphabet": "alphabet",
    "letter": "ex-a1-teachLetter",
    "lesson": "ex-v7-multipleChoice",
    "phrasebook": "phrasebook",
    "show": "show-pb-ak-gamicheret-tu-sheidzleba",
    "dialogue": "dialogue-pd-bazaar",
    "search": ("search-water", "search-woda"),  # English, Polish
    "review": "review",
    "progress": "progress",
}

# The Simulator's island in a 1206 x 2622 screenshot.
CX, Y0, Y1, HALF, PAD = 603, 40, 153, 190, 4


def erase_island(im):
    p = im.load()
    r = (Y1 - Y0) / 2
    cy = (Y0 + Y1) / 2
    src = Y1 + PAD + 3
    for y in range(Y0 - PAD, Y1 + PAD + 1):
        for x in range(CX - HALF - PAD, CX + HALF + PAD + 1):
            dx = max(abs(x - CX) - (HALF - r), 0)
            if math.hypot(dx, abs(y - cy)) <= r + PAD:
                p[x, y] = p[x, src]


def find(folder, lang, look, page):
    if lang == "en":
        hits = glob.glob(os.path.join(folder, f"{look}-[0-9][0-9]-{page}.png"))
        return hits[0] if hits else None
    name = f"polish-{page}.png" if look == "light" else f"polish-dark-{page}.png"
    path = os.path.join(folder, name)
    return path if os.path.exists(path) else None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = sys.argv[1]
    for lang, out in [("en", "shots"), ("pl", "shots/pl")]:
        os.makedirs(os.path.join(ROOT, out), exist_ok=True)
        made = []
        for name, page in PAGES.items():
            if isinstance(page, tuple):
                page = page[0] if lang == "en" else page[1]
            for look in ("light", "dark"):
                src = find(folder, lang, look, page)
                if not src:
                    print(f"  missing: {lang} {look} {page}")
                    continue
                im = Image.open(src).convert("RGB")
                if im.size != (1206, 2622):
                    print(f"  unexpected size {im.size}: {src}")
                    continue
                erase_island(im)
                im.resize((603, 1311), Image.LANCZOS).save(
                    os.path.join(ROOT, out, f"{name}-{look}.webp"), "WEBP", quality=82, method=6)
                made.append(f"{name}-{look}")
        print(f"{lang}: {len(made)} screens in {out}/")


if __name__ == "__main__":
    main()
