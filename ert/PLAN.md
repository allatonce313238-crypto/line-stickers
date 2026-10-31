# Ert LINE Stickers — plan

New chat? Read this whole file first, then continue from **Status**.
Based on the MawKorn plan (`mangkorn/PLAN.md` on branch `claude/line-stickers-bg-dicut-302vim`) and the lessons learned there.

## The project

- Character: **Ert**, chibi black cat Great Wizard of the Fluffy Party (see Character design).
- Format: **16 static LINE stickers** (no animation, no Kling).
- Style: **16-bit pixel art** with bold dark outlines, bright saturated colors, cute chibi proportions (same look as MawKorn and Mx).
- Repo: `allatonce313238-crypto/line-stickers`, branch `claude/blissful-archimedes-o1wbwm`, folder `ert/`.

## Folder layout

| Path | What goes there |
|---|---|
| `ert/references/` | The user's original Ert images, approved design sheets, combined attach images |
| `ert/incoming/` | Every raw ChatGPT image, named `NN-name-vN.png` (keep rejected ones, add a short reason to the name) |
| `ert/prompts/` | One prompt per sticker `NN-name.md`, shared rules in `_common.md` |
| `ert/stickers/` | Approved, cleaned stickers `NN-name.png` |

## Status (2026-10-31)

- Decided: 16 static stickers, 16-bit pixel art, folder `ert/` on this branch.
- Reference images received and saved to `ert/references/`:
  - `earth-thank-you.png`: sticker, cheerful, holding the staff. Plain dark-grey fluffy tail.
  - `earth-thinking.png`: sticker, paw on chin, with a "..." bubble and a loading icon. Brown-and-black ringed tail.
  - `earth-annoyed.png`: sticker, ">_<" eyes, anger mark, lightning bolts. Ringed tail.
  - `earth-wizard-scene.png`: wide fantasy scene casting a spell, full outfit visible.
  - `fluffy-party-poster.png`: Fluffy Party poster. Earth = 2nd member, "Great Wizard".
- These references have text, speech bubbles and white die-cut borders. The new stickers must NOT have them.
- Decided: public name **Ert** (titles, descriptions, prompts, file names). The reference file names keep "earth" (the poster's spelling).
- Decided: 16 stickers, list below.
- `tools/make_sticker.py` copied from `claude/line-stickers-bg-dicut-302vim`. It needs `numpy`, `scipy`, `Pillow` (`pip install scipy` if missing). Watch: its "lime-yellow" cleanup removes pale yellow pixels with almost no blue that touch the background, so check Ert's yellow hat edges after cleanup.
- Decided: tail = **plain dark-grey fluffy**, same colour as the fur (no rings). Sheets have small labels.
- Sheet 1 prompts written: `ert/sheet1-identity.md` (1A full-body turnaround + arms open + staff, 1B head close-ups + expressions). Attach: `ert/references/attach-sheet1.png`.
- Sheet 1A v1 (`ert/incoming/sheet1a-v1.png`): mostly good; the 3/4 views are wrong (fig 2 faces right but is labelled 3/4 Left, fig 6 is a mirrored Front). Fix prompt in `ert/sheet1-identity.md`. Staff in his left paw (viewer's right) like the original sticker: keep.
- Next step: user runs the Sheet 1A fix prompt → Claude reviews v2.

## Character design (from the references)

- Name: **Ert** (written "Earth" on the poster). Role in Fluffy Party: **Great Wizard**.
- Species: chibi **black fluffy cat** wizard (cat face, not a human).
- Face: round cat face, big round **amber-gold eyes** with white shine, small pink nose, small ":3" cat mouth (pink tongue when happy), pink blush, thin whiskers.
- Fur: dark charcoal-black, fluffy and spiky (tufts on the cheeks and head); upright cat ears with pink insides.
- Hat: big floppy **golden-yellow wizard hat** with a bent pointed tip and a wide brim; **blue band with small gold stars**; a gold star emblem with a blue gem on the band.
- Robe: **royal-blue wizard robe and cape** with gold trim and gold star/rune patterns, a high collar, a **gold brooch with a blue gem** at the neck, cream inner panel with gold runes.
- Belt: brown leather belt with a gold buckle, a small pouch and a small brown book on the hip.
- Feet: brown boots with gold trim (`earth-thinking.png`).
- Staff: **gold staff** with a glowing **blue crystal orb** held in a gold crescent or ring at the top (Ert always carries it).
- Tail: ONE plain fluffy tail, same dark charcoal-black as the fur, no stripes or rings.
- Proportions: chibi, head about half of the total height (like the stickers).

### Colour palette (sampled from the reference stickers; approximate, from compressed images)

| Part | Hex |
|---|---|
| Eye highlight / main | `#FBD520` |
| Eye mid | `#C3950A` |
| Eye dark | `#77320A` |
| Fur | `#30232A` |
| Hat yellow | `#FDCE43` |
| Hat shading | `#DF862D` |
| Robe blue light | `#1A7CED` |
| Robe blue dark | `#0842AF` |
| Tongue | `#FA977E` |

### Must never change

Black cat, amber eyes, yellow wizard hat with blue starry band, blue robe with gold trim, blue gem brooch, gold staff with blue orb.

## Steps

1. **References:** save the user's Ert images to `ert/references/`. Sample the main colours in code.
2. **Sheet 1 (identity):** front, 3/4, side, back view + 6 expressions + colour palette. Review it against the references and fix it until the user approves → `ert/references/sheet1-identity-final.png`.
3. **Sheet 2 (poses):** about 9–12 sticker poses drawn from Sheet 1 only (a new ChatGPT chat, so it does not copy older images) → `ert/references/sheet2-poses-final.png`.
4. **Attach image:** combine Sheet 1 and Sheet 2 into one image → `ert/references/attach-stickers.png` (the same attachment for every sticker).
5. **Stickers 01–16:** one at a time (see Workflow per sticker).
6. **Final:** main image 240×240, chat tab image 96×74, check every file against the LINE rules, build the ZIP.

## Workflow per sticker

1. Claude writes the ChatGPT prompt, **gives it in the Claude chat in a code block**, and saves it to `ert/prompts/NN-name.md` as a record. Do NOT tell ChatGPT to read files from GitHub.
2. The user attaches `attach-stickers.png` in ChatGPT, pastes the prompt, and attaches ChatGPT's image in the Claude chat → Claude saves it to `ert/incoming/NN-name-vN.png`.
3. Claude reviews the **raw** image with the checklist below and gives a short fix list (plus a fix prompt if needed). **No background removal or previews before approval** (saves tokens).
4. The user approves → Claude removes the green, trims, fits it into 370×320 with a 10 px margin (even width and height), checks it on white and dark backgrounds → `ert/stickers/NN-name.png`.
5. Commit and push after each step. Update **Status** in this file.

## Review checklist (every image)

1. **Face vs Sheet 1:** same face shape, eye shape and colour, features, hair/ears, accessories. Ert must stay recognisable at small size.
2. **Anatomy:** correct number of arms, legs, fingers/paws; nothing extra, nothing missing; parts attached in the right place.
3. **Pose and expression:** matches the prompt, reads clearly at small size, not the same layout or eyes as an earlier sticker.
4. **Set fit:** its meaning is clearly different from the other stickers (e.g. Thank you vs Sorry).
5. **Rules:** no text, no white border, green background, no green on the character, no white effects touching the green.
6. **After cleanup:** check the transparent PNG on white and dark for holes, leftover green fringe, erased white parts.

## Prompt rules (to go into `ert/prompts/_common.md`)

- Ends with a fixed block: keep the design IDENTICAL to the attached sheets; same 16-bit pixel art; ONE sticker, square 1:1, full body, centered, empty space around; solid flat pure green `#00FF00` background, no shadow or floor; NO text, letters or speech bubbles; NO white border; do not copy an earlier sticker's pose.
- Never put the sticker name in quotes (ChatGPT draws it as text). Describe the meaning instead.
- Effects: yellow, orange or red, never white (white touching green gets erased) and never green.
- Proportions: match the sheets. Never write "head as big as the body".
- **Facing:** front view, or 3/4 with the face and eyes turned to the viewer, so Ert looks at the reader on both sides of the chat (sent stickers show on the right, received on the left).

## Rules from the user (follow every time)

- Give every ChatGPT prompt in a code block in the Claude chat.
- Review every image thoroughly; do not just accept what ChatGPT drew.
- No background removal or previews until the user approves the image.
- Keep replies short.
- No text or speech bubbles in the art, no white border.
- Never send anything to Kling without an explicit "go" (not needed for this set).
- Never change Notion unless the user says so.
- Do not assume. If unsure, ask.
- The user sometimes types English on a Thai keyboard (e.g. "ฟยยพนอำ" = "approve").

## LINE sticker rules (https://creator.line.me/en/guideline/sticker/)

- 8 / 16 / 24 / 32 / 40 stickers per set.
- Each sticker: PNG, max 370×320 px, even width and height, ≤ 1 MB, transparent background, about 10 px margin, RGB, ≥ 72 dpi.
- Main image 240×240, chat tab image 96×74 (each ≤ 1 MB).
- ZIP ≤ 60 MB.
- Check the guideline page again before submitting.

## The 16 stickers

| No. | Sticker | Pose idea |
|---|---|---|
| 01 | Hello | Waves one hand, big smile |
| 02 | On my way! | Running forward, speed lines |
| 03 | OK | Holds up a red O sign |
| 04 | No | Holds up a blue X sign |
| 05 | Thank you | Bows politely |
| 06 | Sorry | Head down, hands together, sweat drop |
| 07 | Love | Holds a big heart |
| 08 | LOL | Laughing hard, holding the belly |
| 09 | Excited | Jumping with sparkles |
| 10 | Surprised | Jumps back, eyes wide |
| 11 | Crying | Big tears (the only sticker with tears) |
| 12 | Angry | Stomping, steam puffs |
| 13 | Fighting! | Fists up, determined |
| 14 | Tired | Lying flat, exhausted |
| 15 | Hungry / So full | TBD |
| 16 | Staring | Deadpan stare at the viewer |
