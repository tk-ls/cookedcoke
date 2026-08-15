# Product photos

Drop transparent PNGs in this folder using the exact filenames below. The site
picks them up automatically — no code change needed. Until a file exists, that
slot falls back to a drawn stand-in, so the page never looks broken.

Twenty-six facings across six shelves.

## Shelf 01 — Classics

| Filename | Product |
|---|---|
| `coke.png` | Coke |
| `fanta.png` | Fanta |
| `sprite.png` | Sprite |
| `solo.png` | Solo |

## Shelf 02 — Minis

| Filename | Product |
|---|---|
| `coke-mini.png` | Coke Mini |
| `fanta-mini.png` | Fanta Mini |
| `sprite-mini.png` | Sprite Mini |

Solo has no mini, so there are three here rather than four.

## Shelf 03 — Chi Forest

| Filename | Product |
|---|---|
| `chi-white-peach.png` | White Peach |
| `chi-lychee-fizzy.png` | Lychee Fizzy |
| `chi-grape-delight.png` | Grape Delight |
| `chi-green-apple.png` | Green Apple |
| `chi-watermelon.png` | Watermelon |
| `chi-guava.png` | Guava Flavour |
| `chi-orange.png` | Orange Flavour |
| `chi-bamboo-grapefruit.png` | Bamboo Grapefruit |
| `chi-pomelo-zest.png` | Pomelo Zest |

## Shelf 04 — Tea & Yoosh

| Filename | Product |
|---|---|
| `iced-black-tea.png` | Iced Black Tea |
| `yoosh.png` | Yoosh |
| `yoosh-lychee.png` | Yoosh Lychee |

## Shelf 05 — Chef Kang

| Filename | Product |
|---|---|
| `chef-kang-regular.png` | Regular |
| `chef-kang-hot-spicy-beef.png` | Hot & Spicy Beef |
| `chef-kang-seafood.png` | Seafood |
| `chef-kang-pickled-veg-beef.png` | Pickled Vegetables Beef |
| `chef-kang-pork-shallots.png` | Pork with Fried Shallots |

## Shelf 06 — Snacks

| Filename | Product |
|---|---|
| `red-rock-deli.png` | Red Rock Deli |
| `mamee-bbq.png` | Mamee BBQ |

## Shoot your own

Use your own photos rather than pulling images off Woolworths or a brand site —
those are someone else's copyright and this repo publishes to a public domain.
Your own shots are also just better, because they're the actual stock.

1. Stand the item on a desk against a plain, evenly lit wall. A sheet of white
   A4 taped to the wall works fine.
2. Shoot straight on, roughly level with the middle of the can, not looking down
   at it. Keep the camera in the same spot for every item so they end up at
   consistent scale.
3. Fill the frame vertically but leave a little air top and bottom.
4. Daylight from a window beats overhead fluorescents. Avoid flash — it blows
   out the label and kills the highlight down the side of the can.

Shoot the minis in the same session as the full-size cans, from the same spot,
so the size difference between them is real rather than something the page has
to fake.

## Cut the background out

On this Mac, no extra software needed:

- Select the photos in Finder → right-click → **Quick Actions → Remove
  Background**. macOS writes a transparent PNG next to each original.
- If Remove Background isn't in the menu, open the photo in Preview → Tools →
  **Instant Alpha**, drag over the background, delete, then export as PNG.

Then rename each file to match the tables above and drop it in this folder.

## Make them consistent

Photos straight off a phone vary in crop and size, which makes the shelf look
uneven. `tools/normalize.py` in the repo root trims each image to its content,
scales it to a common height, and centres it on a fixed canvas so everything
sits properly on the shelf. See that file for how to run it.

Note that it scales every image to the same height, which would erase the
difference between a full-size can and a mini. Run it on the full-size items,
then run it on the minis separately with a smaller `--tall-ratio`, or just skip
it for the minis and crop those by hand.

## What the page does with them

Each image is drawn with `object-fit: contain` and bottom-aligned, so the base
of the product meets the glass shelf. Tall items (bottles) and short items
(noodle packs) can therefore be different heights in the same row and still look
like they're standing on the same surface — no need to pad them to match.
