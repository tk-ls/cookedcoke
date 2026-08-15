#!/usr/bin/env python3
"""Make cut-out product photos consistent enough to sit on one shelf.

Phone photos vary in crop and scale, which makes the shelf row look ragged.
This trims each PNG to its opaque content, scales it to a common height, and
centres it on a fixed-width transparent canvas with the product sitting on the
bottom edge — which is where the page expects it, since facings are
bottom-aligned against the glass shelf.

Setup (once):

    python3 -m pip install --user pillow

Usage, from the repo root:

    python3 tools/normalize.py products/*.png

Files are rewritten in place, so work on copies or commit first. Pass
--dry-run to see what it would do without writing anything.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Pillow is not installed. Run:\n"
        "    python3 -m pip install --user pillow"
    )

# The canvas every product lands on. Cans end up near full height; snack packs
# and apples stay short, which is correct — they really are shorter.
CANVAS_W = 600
CANVAS_H = 900
# Fraction of canvas height a full-height item (a tall can or bottle) occupies.
TALL_RATIO = 0.94
# Breathing room either side, as a fraction of canvas width.
SIDE_PAD = 0.06


def trim(img: Image.Image) -> Image.Image:
    """Crop away fully transparent margins."""
    alpha = img.getchannel("A")
    box = alpha.getbbox()
    if box is None:
        raise ValueError("image is fully transparent — did the cut-out work?")
    return img.crop(box)


def normalize(path: Path, dry_run: bool = False) -> str:
    img = Image.open(path).convert("RGBA")
    before = img.size

    img = trim(img)
    tw, th = img.size

    # Scale to the target height, then pull back if that makes it too wide.
    target_h = int(CANVAS_H * TALL_RATIO)
    scale = target_h / th
    max_w = int(CANVAS_W * (1 - 2 * SIDE_PAD))
    if tw * scale > max_w:
        scale = max_w / tw

    new_size = (max(1, round(tw * scale)), max(1, round(th * scale)))

    if dry_run:
        return f"{path.name}: {before} -> trim {(tw, th)} -> {new_size} on {(CANVAS_W, CANVAS_H)}"

    img = img.resize(new_size, Image.LANCZOS)

    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    # Horizontally centred, sitting on the bottom edge.
    canvas.paste(img, ((CANVAS_W - new_size[0]) // 2, CANVAS_H - new_size[1]), img)
    canvas.save(path, "PNG", optimize=True)

    return f"{path.name}: {before} -> {(CANVAS_W, CANVAS_H)}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path, help="PNG files to normalize, in place")
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    args = ap.parse_args()

    failures = 0
    for path in args.files:
        if path.name.lower() == "readme.md":
            continue
        try:
            print(normalize(path, args.dry_run))
        except Exception as exc:  # noqa: BLE001 - report and keep going
            print(f"{path.name}: SKIPPED — {exc}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
