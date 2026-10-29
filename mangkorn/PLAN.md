# MawKorn LINE Stickers — plan

New chat? Read this whole file first, then continue from **Status**.

## The project

- Character: **Mangkorn**, a chibi red fluffy dragon. Public name: **MawKorn** (use MawKorn in titles, descriptions and file names).
- Second character in the **Fluffy Party** series, after Mx (Mx's animated emoji set is finished, in `allatonce313238-crypto/team-kpi-dashboard`, branch `claude/line-stickers-bg-dicut-302vim`, folder `line-stickers/`).
- Format: **16 static LINE stickers** (no animation, no Kling).
- Work goes in `mangkorn/stickers/`, one file per sticker (`01-hello.png`, …).

## Status (2026-10-29)

- Decided: LINE stickers (not emoji), 16 stickers, static, this repo.
- Decided: sticker 16 = Hug (small Mx doll). **No white border** (only the character's own dark pixel-art outline).
- Decided: make **Sheet 1, then Sheet 2** first; use them as references for every sticker.
- Next: Sheet 1 prompt given to the user, waiting for their image.

## Rules from the user (follow every time)

1. **Never send anything to Kling without an explicit "go".** (Not needed for this set.)
2. **Never change Notion until the user says so.**
3. Put every prompt in a code block so it can be copied.
4. **No speech bubbles or text** in the art.
5. Do not assume. If unsure, ask.
6. The user sometimes types English on a Thai keyboard (e.g. "ฟยยพนอำ" = "approve").

## Workflow per sticker

1. I write a ChatGPT prompt; the user makes the image in ChatGPT and sends it. Pure green (#00FF00) background, no text.
2. I remove the green, trim, and fit it into 370×320 with a 10 px margin (even width and height), then send a preview.
3. User approves → saved as `mangkorn/stickers/NN-name.png`.
4. At the end: main image (240×240), tab image (96×74), validation, ZIP.

## LINE sticker rules (official guideline: https://creator.line.me/en/guideline/sticker/)

- 8 / 16 / 24 / 32 / 40 stickers per set.
- Each sticker: PNG, max 370×320 px, even width and height, ≤ 1 MB, transparent background, about 10 px margin, RGB, ≥ 72 dpi.
- Main image 240×240, chat tab image 96×74 (each ≤ 1 MB).
- ZIP ≤ 60 MB.

## References

- `team-kpi-dashboard` (branch above): `line-stickers/full-res/08.png` (MawKorn standing, "Fighting!", main design reference), `line-stickers/full-res/07.png` (sleeping).
- Dragon stickers from the Mx-era set: `line-stickers/full-res/07.png` (zZZ), `08.png` (Fighting!), `09.png` (Hungry).
- Mx doll for the Hug sticker: `line-stickers/animated-emoji/16-hug/kling-start.png`.
- Design: red scales with cream fluffy fur, dark curved horns with gold bands, gold crown with a red gem, red wings with gold edges, fluffy tail with gold spikes, big amber eyes, small fangs.
- `mangkorn/sheet1-identity.md`, `mangkorn/sheet2-poses.md`: design-sheet prompts (optional, for consistency).

## The 16 stickers

| No. | Sticker | Pose |
|---|---|---|
| 01 | Hello | Waves one clawed paw, wings slightly open |
| 02 | On my way! | Flying forward, wings beating, speed lines |
| 03 | OK | Holds up a red O sign |
| 04 | No | Holds up a blue X sign |
| 05 | Thank you | Bows, paw on chest, wings folded |
| 06 | Sorry | Bows low, ears and wings drooping |
| 07 | Please | Paws together, big shiny eyes |
| 08 | Love | Makes a heart with his tail and paws |
| 09 | LOL | Sitting down, laughing hard, pointing one claw forward |
| 10 | Excited | Jumping, wings flapping, sparkle eyes |
| 11 | Surprised | Jumps back, crown popping up |
| 12 | Crying | Big tears, tiny sobbing smoke puffs |
| 13 | Angry | Stomping, small burst of fire, steam from the ears |
| 14 | Fighting! | Fists up, breathing fire (like `full-res/08.png`) |
| 15 | Tired | Lying flat, exhausted |
| 16 | Hug | Hugs a small round Mx plush doll (dot eyes, no mouth) |

Not wanted in the 16: Good morning, Good night.
