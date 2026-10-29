# Mangkorn: Sheet 2, Key poses

Purpose: lock the body poses the 16 stickers need, so the dragon stays consistent. Every pose maps to one or more stickers (see the table at the end).

Attach in ChatGPT (it cannot read images from this private repo; Claude sends them in the Claude chat):
- `mangkorn/references/sheet1-identity-final.png` (the approved identity sheet)
- `mangkorn/references/dragon-fighting.png`
- `mangkorn/references/dragon-hungry.png`

## Prompt

```
Using the attached character identity sheet AND the attached dragon images as the exact character reference, create ONE pose reference sheet, landscape 3:2, plain flat white background, the same 16-bit pixel art style with bold dark outlines, cute chibi proportions. The dragon must look IDENTICAL in every pose: same face, amber eyes, horns with gold bands, gold crown with red gem, red scales with gold diamond studs, cream fluffy fur, dark brown hand paws, pink-padded feet, red wings with gold edges, fluffy red-and-cream tail. Ignore the text, speech bubbles and effects in the dragon images.

Grid of 12 poses, 4 columns x 3 rows, every pose the same size. Draw every pose full body in a 3/4 front view (body turned halfway, face toward the viewer), unless the pose says otherwise.
Row 1:
1) Standing upright, relaxed, arms down, wings folded, calm closed-mouth smile.
2) Standing, waving one paw high above his head, happy smile.
3) Flying forward, wings spread wide and beating, body leaning forward, tail streaming behind.
4) Standing, holding a BLANK round white sign above his head with both paws (nothing written on it).
Row 2:
5) Bowing forward politely, one paw on his chest, wings folded.
6) Both paws pressed together under his chin, pleading, big shiny eyes.
7) Both paws making a heart shape in front of his chest, happy smile.
8) Sitting on the ground, laughing hard with eyes squeezed shut, pointing one claw forward at the viewer.
Row 3:
9) Jumping, both fists pumping up, wings flapping, excited open-mouth smile.
10) Jumping back in surprise, both paws up near his cheeks, mouth open.
11) Lying flat on his belly, completely exhausted, arms and wings spread out limp, half-closed eyes.
12) Standing, hugging a small round plush doll with both arms, happy closed eyes (the doll is a simple round blob shape with dot eyes and no mouth).

No tears on any pose. Text: only a small number under each pose (1 to 12). No other text, no speech bubbles. No scenery, no ground shadow.
```

## Which sticker uses which pose

| Pose | Stickers |
|---|---|
| 1 Standing, neutral | base for Angry, Crying, Fighting! |
| 2 Waving | 01 Hello |
| 3 Flying | 02 On my way! |
| 4 Blank sign | 03 OK (red O on the sign), 04 No (blue X on the sign); the O / X is drawn per sticker |
| 5 Bowing | 05 Thank you, 06 Sorry |
| 6 Paws together | 07 Please |
| 7 Paw heart | 08 Love |
| 8 Sitting, laughing, pointing | 09 LOL |
| 9 Jumping, fists up | 10 Excited, 14 Fighting! |
| 10 Surprised | 11 Surprised |
| 11 Lying flat | 15 Tired |
| 12 Hugging a doll | 16 Hug |

## After making the image

Attach the finished image in the Claude chat; Claude saves it to `mangkorn/incoming/sheet2-poses-v1.png`.
