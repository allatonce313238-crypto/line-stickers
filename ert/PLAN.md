# Ert LINE Stickers — plan

New chat? Read this whole file first, then continue from **Status**.
Based on the MawKorn plan (`mangkorn/PLAN.md` on branch `claude/line-stickers-bg-dicut-302vim`) and the lessons learned there.

## The project

- Character: **Ert**. Design: **to be filled in from the user's reference images** (not received yet).
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
- **Waiting for:** the user's existing Ert reference images.
- **Open question:** `tools/make_sticker.py` (green removal, trim, fit to 370×320) is only on branch `claude/line-stickers-bg-dicut-302vim`. Copy it to this branch? (ask)
- Next step: save the reference images to `ert/references/`, fill in **Character design** below, then write the Sheet 1 prompt.

## Character design (fill in from the references)

- Species / type: TBD
- Face (shape, eyes, eye colour hex, nose, mouth): TBD
- Hair / ears / head features: TBD
- Body and proportions: TBD
- Clothes / accessories: TBD
- Colour palette (sample hex values from the reference, do not guess): TBD
- Things that must never change: TBD

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

## The 16 stickers (DRAFT: confirm or change with the user)

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
