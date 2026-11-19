---
name: botkits-scene-detail-board
description: >-
  Use this when you want one portrait image that pairs a real-looking photo of a
  scene, place, product or person with a grid of small hand-sketched tiles, each
  showing one detail from that photo. Plans the details, the palette and the
  layout, then writes a plain-text image prompt and checks the result. Text in
  the image stays short, because image models misspell words.
---
# Scene detail board

Make one portrait image in two zones. The top zone is a photo of the subject. The bottom zone is a paper sheet with a short title and a grid of small sketches. Each sketch picks one detail out of the photo and draws it by hand, in a few flat colors taken from the photo.

The board works for any subject: a street corner, a product on a table, a dish, a room, a trail, a pet, a market stall, a workshop.

## 1. Ask for the inputs

Ask once. Use the defaults for anything the user does not give.

| Input | Default | Options |
| --- | --- | --- |
| Subject | none, ask | Any scene, place, object, product, animal or person |
| Photo | generate it | Use a photo the user gives you |
| Shape | 4:5 portrait | 3:4, 2:3, 9:16 |
| Tiles | 6 (2 rows of 3) | 4 (2 by 2), 9 (3 by 3) |
| Sketch look | ink and wash | two-color print, pencil and crayon, line only |
| Title | you propose 2 to 4 words | The user's words |
| Where it goes | a social post | poster, blog header, product page |

If the photo shows a real, identifiable person, ask if you may use it. Do not draw a real person's face from someone else's photo.

## 2. List the details

Look at the photo (or the scene you will generate) and list more details than you need. Then keep the tile count. Use this ladder so the tiles are not all the same size of thing:

1. The whole subject, small and simple.
2. One material or surface (wood grain, fabric, foam, stone).
3. One part you can hold (a handle, a cup, a key, a leaf).
4. The light or the weather (sun patch, rain, steam, shadow).
5. One sign of motion or sound (wind lines, a bell, a wave, a wheel).
6. One thing that says where this is (a sign shape, a tile pattern, a plant).
7. One small surprise that is really in the photo.

Rules for the list:

- One detail per tile. No tile repeats another.
- Every detail is visible in the photo. Do not add objects that are not there.
- Keep at least one tile wide and at least one tile very close.
- No brand logos and no readable words inside the tiles.

## 3. Pick the palette

Take 3 or 4 colors from the photo: one dark, one light, one or two mid colors. The sketches use only these colors plus black ink and the paper tone. Write the colors as plain names and, if you can sample them, as hex values. Show them on the board as small square chips.

## 4. Plan the layout

Use this layout unless the user asks for another.

- **Photo zone:** the top 55% of the image, full width, no border. Natural light. Real lens look. The subject sits in the middle third.
- **Paper zone:** the bottom 45%, warm off-white paper with a light grain.
- **Title row:** at the top of the paper zone, left aligned. The title in a light, narrow sans serif, all capitals, thin strokes. Under it, one thin rule across the width.
- **Tile grid:** under the title row, centered, with equal gaps. Tiles are squares with softly rounded corners. Each tile has a flat color background from the palette.
- **Tile numbers:** a small number under each tile (01, 02, 03 and so on) in a small monospace face. No other words under the tiles.
- **Footer row:** the palette chips at the bottom right. Leave the bottom left empty.
- Keep wide margins. Empty paper is part of the look.

## 5. Set the sketch look

| Look | Line | Fill | Texture |
| --- | --- | --- | --- |
| Ink and wash (default) | Loose black ink, slightly uneven, as if drawn by hand | Flat washes from the palette, a little outside the lines | Paper grain shows through |
| Two-color print | Dark palette color, no black | Two palette colors with small misregistration | Fine dot grain |
| Pencil and crayon | Soft graphite | Crayon strokes in the palette | Waxy, uneven |
| Line only | Black ink | None, paper shows | Paper grain |

All tiles use the same look. The sketches are simple and a little naive, not technical drawings. The photo stays a photo. It is not sketched.

## 6. Write the prompt

Fill this template. Keep it in one block, in this order: shape, photo zone, paper zone, tiles, look, text, limits.

```text
A [SHAPE] portrait image in two zones.
Top [55%]: a natural photo of [SUBJECT AND SETTING], [LIGHT], real lens look, subject in the middle.
Bottom [45%]: warm off-white paper with light grain and wide margins.
At the top of the paper, left aligned: the title "[TITLE]" in a light, narrow, thin all-caps sans serif, with one thin rule under it.
Below it, a centered grid of [ROWS] by [COLUMNS] rounded square tiles with equal gaps. Each tile is a small, simple hand sketch of one detail from the photo:
01 [DETAIL], 02 [DETAIL], 03 [DETAIL], 04 [DETAIL], 05 [DETAIL], 06 [DETAIL].
Sketch look: [LOOK ROW FROM STEP 5]. Colors only [PALETTE] plus black ink and the paper tone.
Under each tile, its small number in a monospace face. Bottom right: [N] small square color chips of the palette.
No other text. No logos. No watermark. No borders around the photo.
```

If the user gave a photo, pass it to the model as the reference for the top zone and say "keep the photo unchanged" in the prompt.

## 7. If the text comes out wrong

Image models often misspell words. If the title or the numbers are wrong after two tries:

1. Ask the model for the board with no title and no numbers.
2. Add the title, numbers and chips yourself in an HTML or SVG layer over the image, using real fonts.
3. Export the final PNG from that layer.

## 8. Check the result

Open the image at full size and check each item. Fix and regenerate once per failed item. Stop after three attempts and show the best one with the list of misses.

- [ ] Shape and zone split match the plan.
- [ ] Tile count is right. Each tile shows one detail, and each detail is in the photo.
- [ ] No tile repeats another, and the ladder has a wide tile and a close tile.
- [ ] Only the palette colors, black ink and paper are in the tiles.
- [ ] The title is spelled right. The numbers are in order. No extra text appeared.
- [ ] No logos, no watermark, no readable brand names.
- [ ] Faces of real people only with permission.

## 9. Hand over

Give the user:

- the final image,
- the filled prompt,
- the detail list and the palette, so they can make a matching board later.

If the photo zone was generated, do not call it a real photo when you post it. Follow the platform's rules for labeling AI images.
