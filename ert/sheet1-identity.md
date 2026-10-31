# Ert: Sheet 1, identity (2 images)

Purpose: lock Ert's look from every angle so every sticker stays consistent. Reference sheets, not stickers.

Split into 2 images (fewer figures per image = more consistent, more detail):
- **Sheet 1A**: full-body turnaround + arms open + with staff + staff alone.
- **Sheet 1B**: head close-ups from every angle + expressions.

Attach: `ert/references/attach-sheet1.png` (left: the Thank you sticker without its text, right: the wizard scene crop).
Make 1A first. Make 1B in the same ChatGPT chat after 1A is approved, with 1A attached too.

Lessons from MawKorn's sheet: ChatGPT added tears everywhere, skipped the 3/4 view and drew the wrong eye colour. The prompts say all three explicitly.

## Prompt: Sheet 1A (full body)

```
The attached image shows my character Ert, a chibi black cat wizard (left: a sticker, right: a scene). Ignore the background, sparkles, hearts and magic effects; use only the character.

Create ONE character turnaround reference sheet, landscape 16:9, plain flat white background, 16-bit pixel art with bold dark outlines and bright saturated colors, cute chibi proportions (head about half of the total height). The character must look IDENTICAL in every figure: same size, same proportions, same colors, same outfit details, all standing on the same invisible ground line.

Character design (keep exactly):
- Black fluffy cat with dark charcoal-black fur, spiky fluffy tufts on the cheeks and head, upright cat ears with pink insides, thin whiskers.
- Round cat face, big ROUND amber-gold eyes (yellow-orange, never blue) with a white shine, small pink nose, small cat mouth, light pink blush.
- Big floppy golden-yellow wizard hat with a wide brim and a bent pointed tip; a royal-blue hat band with small gold stars; a gold star-shaped emblem with a round blue gem on the band.
- Royal-blue wizard robe with a short cape and wide sleeves, gold trim and gold star patterns, a cream inner front panel with gold cross patterns, a gold round brooch with a blue gem at the collar.
- Brown leather belt with a gold buckle, a small brown book-pouch with a blue gem on the hip.
- Black cat paws as hands (no gloves). Brown boots with gold trim.
- ONE plain fluffy tail, the same dark charcoal-black as his fur, no stripes, no rings.

Layout, two rows:
Top row, six full-body standing views, arms relaxed at his sides, calm neutral face, NO staff:
Front, 3/4 Left (body turned halfway toward the viewer's left), Left Side (pure profile facing the viewer's left), Back, Right Side (pure profile facing the viewer's right), 3/4 Right (body turned halfway toward the viewer's right).
Bottom row, three figures:
1. Front view, both arms stretched wide open to the sides (T-pose), calm face, no staff.
2. Front view, holding his staff upright in his right paw, happy smile.
3. The staff alone, upright: a gold staff with a gold curled top holding a glowing round blue crystal orb.

In the Back view show the back of the hat, the cape, and the tail coming from his lower back.
In the side views show exactly ONE eye and ONE ear on the visible side in the correct place.

NO tears anywhere. No scenery, no shadows, no floor, no extra characters.
Text: only a small plain label under each figure: Front, 3/4 Left, Left Side, Back, Right Side, 3/4 Right, Arms Open, With Staff, Staff. No other text, no logos, no speech bubbles.
```

## Prompt: Sheet 1B (head close-ups)

Attach `attach-sheet1.png` and the approved Sheet 1A.

```
Use the attached approved Sheet 1A as the exact design for Ert (the attached sticker and scene are extra reference). Ignore any background or effects.

Create ONE head close-up reference sheet, landscape 16:9, plain flat white background, the SAME 16-bit pixel art style, bold dark outlines, bright saturated colors. Every head must be the same size, same hat, same face, same colors as Sheet 1A.

Each close-up shows the head with the full wizard hat and the top of the robe collar with the gold blue-gem brooch.

Top row, six head angles, calm neutral face, eyes open:
Front, 3/4 Left, Left Side, Back, Right Side, 3/4 Right
(3/4 = head turned halfway, face still visible; Side = pure profile; Back = back of the head and hat, no face.)

Bottom row, six front-view expressions:
Happy (big smile, eyes open), Laughing (eyes closed ^ ^, mouth open), Sad (droopy ears, frown, NO tears), Angry (frown, furrowed brows), Surprised (eyes wide, small round mouth), Sleepy (half-closed eyes).

Eyes: big ROUND amber-gold with a white shine (never blue), unless the expression says closed or half-closed.
NO tears anywhere. No scenery, no shadows, no extra characters.
Text: only a small plain label under each head: Front, 3/4 Left, Left Side, Back, Right Side, 3/4 Right, Happy, Laughing, Sad, Angry, Surprised, Sleepy. No other text, no logos.
```

## After each image

Attach ChatGPT's image in the Claude chat. Claude saves it to `ert/incoming/sheet1a-vN.png` / `sheet1b-vN.png`, reviews it, and gives a fix list.

## Checks when reviewing

- Same size and proportions in every view; head about half the height.
- Side views: one eye, one ear, nose and mouth in profile, hat brim correct.
- Back view: tail plain black (no rings), cape, back of the hat.
- 3/4 views really turned (not a copy of Front).
- Eyes amber, no tears, no blue gloves (the scene's glowing hand is magic, not a glove).
- Staff matches the sticker version (gold curl holding the blue orb).

## Sheet 1A v1 review (`ert/incoming/sheet1a-v1.png`)

Good: same size and proportions everywhere, amber eyes, no tears, plain black tail, outfit matches the reference, staff matches the sticker (gold curl + blue orb + blue crystal tip), Front, Left Side, Back, Arms Open, With Staff all fine.
With Staff holds the staff in his LEFT paw (viewer's right), same as the original Thank you sticker: keep it.

Problems:
1. Figure 2 ("3/4 Left") actually faces the viewer's RIGHT (nose and mouth right of centre, far eye on the right).
2. Figure 6 ("3/4 Right") is NOT turned: it is the Front view mirrored (face straight on; hat emblem and tail flipped to the other side).
→ There is no 3/4 view facing the viewer's left.

Minor (accepted, not worth risking an edit): side views do not show the hat emblem / book-pouch on the correct side; Back hat tip curls the same way as Front.

## Fix prompt: Sheet 1A v1 → v2

Attach `ert/incoming/sheet1a-v1.png` (+ `attach-sheet1.png`).

```
Edit the attached Ert turnaround sheet. Keep everything else EXACTLY the same: layout, size, style, colors, every other figure and label. Change only these two things:

1. Second figure in the top row: keep the drawing as it is (it faces the viewer's right), only change its label to "3/4 Right".

2. Sixth figure in the top row (far right): it is currently just the Front view mirrored. Redraw it as a real 3/4 view facing the viewer's LEFT: the same character, body and head turned halfway toward the viewer's left, face still visible, nose and mouth shifted toward the viewer's left, the far eye smaller near the edge of the face, the tail visible behind him on the viewer's right. Do not mirror the outfit: the gold star emblem with the blue gem stays on the same side of the hat as in the Front view (the viewer's left side of the hat in Front), the brown book-pouch stays on the same hip as in the Front view. Change its label to "3/4 Left".

Same size, same ground line, same pixel art style, calm neutral face, amber eyes, no tears, no staff. Plain white background. No other text.
```

## Sheet 1A v2 review (`ert/incoming/sheet1a-v2.png`)

Fixed: figure 2 relabelled 3/4 Right (correct), figure 6 is now really turned toward the viewer's left.
New problems in figure 6 (3/4 Left):
1. TWO book-pouches (one on each hip). He has only one.
2. Hat emblem moved to the other side of the hat (mirrored).
Everything else unchanged and fine.

## Optional fix prompt: Sheet 1A v2 → v3

Attach `ert/incoming/sheet1a-v2.png`.

```
Edit the attached Ert turnaround sheet. Keep everything else EXACTLY the same. Change only the last figure in the top row, labelled 3/4 Left:
1. He has only ONE brown book-pouch, on the same hip as in the Front view. Remove the extra book-pouch on the other hip; there the robe continues with its normal blue cloth and gold trim.
2. The gold star emblem with the blue gem must be on the same side of the hat as in the Front view (his right side). Because he is turned toward the viewer's left, the emblem is on the near side of the hat, on the viewer's left part of the band. Remove the emblem from the viewer's right part of the band.
Same pose, size, face, colors and pixel style. No other changes, no other text.
```

## Sheet 1B v1 review (`ert/incoming/sheet1b-v1.png`)

Good: same head size and hat everywhere, amber eyes, no tears, Front / Left Side / Back / Right Side fine; expressions Happy, Laughing, Sad, Angry, Surprised all clear and different.
Problems (same mistake as 1A v1):
1. Head 2 (labelled 3/4 Left) faces the viewer's RIGHT.
2. Head 6 (labelled 3/4 Right) is the Front mirrored, not turned.
Minor: Sad ears are not drooping; Sleepy reads more "unimpressed / deadpan" than sleepy (still useful).

## Fix prompt: Sheet 1B v1 → v2

Attach `ert/incoming/sheet1b-v1.png`.

```
Edit the attached Ert head sheet. Keep everything else EXACTLY the same: layout, size, style, colors, every other head and label. Change only:

1. Second head in the top row: keep the drawing as it is (it faces the viewer's right), only change its label to "3/4 Right".

2. Sixth head in the top row (far right): it is currently the Front head mirrored. Redraw it as a real 3/4 view facing the viewer's LEFT: head turned halfway toward the viewer's left, face still visible, nose and mouth shifted toward the viewer's left, the far eye smaller near the edge of the face. Do not mirror the hat: the gold star emblem with the blue gem stays on his right side of the hat as in the Front head, which is now the near side, on the viewer's left part of the band. Only ONE emblem. Change its label to "3/4 Left".

3. Sad head: make both ears droop down to the sides. No tears.

Same size, same pixel style, amber eyes. Plain white background. No other text.
```

## Sheet 1B v2 review (`ert/incoming/sheet1b-v2.png`)

- Head 6 fixed: real 3/4 view facing the viewer's left, ONE emblem on the near side (correct).
- ChatGPT did NOT relabel head 2 (both said 3/4 Left) → label changed to "3/4 Right" in code (Inter Bold).
- Sad ears still not drooping: accepted (minor).
→ `ert/references/sheet1b-heads-final.png` (pending the user's approval).
