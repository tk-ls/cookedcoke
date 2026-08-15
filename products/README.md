# Product photos

Drop transparent PNGs in this folder using the exact filenames below. The site
picks them up automatically — no code change needed. Until a file exists, that
slot falls back to a drawn stand-in, so the page never looks broken.

| Filename | Shelf | Product |
|---|---|---|
| `coke-zero.png` | 01 | Coke Zero |
| `sprite-zero.png` | 01 | Sprite Zero |
| `fanta-mini.png` | 01 | Fanta Mini |
| `the-red.png` | 01 | The Red (ours) |
| `the-black.png` | 01 | The Black (ours) |
| `chi-white-peach.png` | 02 | Chi Forest White Peach |
| `chi-lychee.png` | 02 | Chi Forest Lychee |
| `chi-grape.png` | 02 | Chi Forest Grape Delight |
| `chi-rotating.png` | 02 | This week's essence |
| `monster-zero.png` | 03 | Monster Zero Sugar |
| `red-bull.png` | 03 | Red Bull |
| `pellegrino.png` | 04 | S.Pellegrino |
| `sodaly.png` | 04 | Sodaly |
| `lipton-peach.png` | 04 | Lipton Peach No Sugar |
| `pocky.png` | 05 | Pocky |
| `pringles.png` | 05 | Pringles |
| `party-mix.png` | 05 | The Natural Party Mix |
| `smiths.png` | 06 | Smith's |
| `rrd-honey-soy.png` | 06 | RRD Honey Soy |
| `apples.png` | 06 | Apples |

## Shoot your own

Use your own photos rather than pulling images off Woolworths or a brand site —
those are someone else's copyright and this repo publishes to a public domain.
Your own shots are also just better, because they're the actual stock.

It takes about ten minutes for all twenty:

1. Stand the item on a desk against a plain, evenly lit wall. A sheet of white
   A4 taped to the wall works fine.
2. Shoot straight on, roughly level with the middle of the can, not looking down
   at it. Keep the camera in the same spot for every item so they end up at
   consistent scale.
3. Fill the frame vertically but leave a little air top and bottom.
4. Daylight from a window beats overhead fluorescents. Avoid flash — it blows
   out the label and kills the highlight down the side of the can.

## Cut the background out

On this Mac, no extra software needed:

- Select the photos in Finder → right-click → **Quick Actions → Remove
  Background**. macOS writes a transparent PNG next to each original.
- If Remove Background isn't in the menu, open the photo in Preview → Tools →
  **Instant Alpha**, drag over the background, delete, then export as PNG.

Then rename each file to match the table above and drop it in this folder.

## Make them consistent

Photos straight off a phone vary in crop and size, which makes the shelf look
uneven. `tools/normalize.py` in the repo root trims each image to its content,
scales it to a common height, and centres it on a fixed canvas so everything
sits properly on the shelf. See that file for how to run it.

## What the page does with them

Each image is drawn with `object-fit: contain` and bottom-aligned, so the base
of the product meets the glass shelf. Tall items (bottles) and short items
(snack packs) can therefore be different heights in the same row and still look
like they're standing on the same surface — no need to pad them to match.
