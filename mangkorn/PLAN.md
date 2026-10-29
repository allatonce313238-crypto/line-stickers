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
- Sheet 1 v1 made (`mangkorn/incoming/sheet1-identity-v1.png`): design matches the references, but tears on almost every face, no 3/4 view, eye swatch labeled blue (marked in `mangkorn/incoming/sheet1-identity-v1-issues.png`). Fix prompt: `mangkorn/sheet1-fix.md` (eye swatch = `#FAB311`, sampled from his real eye). v2 made (`mangkorn/incoming/sheet1-identity-v2.png`, compare: `sheet1-v1-vs-v2.png`): Front tears fixed; faint tears still on Excited/Angry, clear tear on Surprised; still no 3/4 view; eye swatch still blue.
- Sheet 1 **approved**: v2 with the eye swatch fixed in code (amber `#FAB311`) → `mangkorn/references/sheet1-identity-final.png`. Remaining faint tears on some close-ups are accepted; every sticker prompt says "no tears" (except Crying).
- Sheet 2: ChatGPT ignored `sheet2-poses.md` and drew generic game poses; the user **kept it as it is** → `mangkorn/references/sheet2-poses-final.png`.
- Sheet 3 v1 copied Sheet 2's poses (rejected). v2 (new ChatGPT chat, only Sheet 1 attached) has all 9 poses → `mangkorn/references/sheet3-poses-final.png`. Notes for sticker prompts: Sign is a round sign on a stick held in one paw; Love holds a heart instead of making one with paws; Tired looks asleep (Zzz); Hug doll is a cream cat plush with a mouth (use `mx-hug-doll.png` for the real sticker); sheet has a white die-cut border, the stickers must NOT.
- Sticker prompts: `mangkorn/prompts/NN-name.md` (shared rules in `_common.md`); one attach image for all stickers: `references/attach-stickers.png`.
- 01 Hello: v1 had "Hello!" text + white border (removed in code: `tools/make_sticker.py ... --drop 0,0,940,430`) → `mangkorn/stickers/01-hello.png` (370×310). **Approved.**
- 02 On my way!: **tricycle** version chosen. v3 (fix prompt `prompts/02-on-my-way-fix.md`) fixed the floating rear wheel. Feet stay dark brown on top: that matches `dragon-hungry.png` (brown feet, cream soles with pink pads), so the earlier foot note was wrong. → `mangkorn/stickers/02-on-my-way.png` (324×320). Flying v1 kept as `incoming/02-on-my-way-v1-flying-clean.png`. **Approved.**
- 03 OK: v1 repeated the Hello pose (rejected); v2 has the sign with a red O → `mangkorn/stickers/03-ok.png` (326×320). **Approved.**
- Next: 04 No prompt ready; waiting for the image.
- Tool update: stricter green removal + lime-yellow pocket removal; 01–03 re-processed with it.

## Rules from the user (follow every time)

- **Keep replies short (save tokens).** For each ChatGPT step: send ONE combined attach image (`mangkorn/references/attach-<step>.png`) + one short line to paste. Nothing else unless asked.

0. **No copy-paste between chats. Everything goes through files in this repo.** Prompts are saved as files here; ChatGPT (connected to this repo) and new Claude chats read them from the repo. The repo is **public** since 2026-10-29 (user's choice). Prompt files link reference images by raw URL: https://raw.githubusercontent.com/allatonce313238-crypto/line-stickers/claude/line-stickers-bg-dicut-302vim/mangkorn/references/<file>. If ChatGPT still cannot use a link, so: Claude sends the reference images in the Claude chat → the user attaches them in ChatGPT; the user attaches ChatGPT's finished image in the Claude chat → Claude saves it to `mangkorn/incoming/` on this branch.

1. **Never send anything to Kling without an explicit "go".** (Not needed for this set.)
2. **Never change Notion until the user says so.**
3. Put every prompt in a code block so it can be copied.
4. **No speech bubbles or text** in the art.
5. Do not assume. If unsure, ask.
6. The user sometimes types English on a Thai keyboard (e.g. "ฟยยพนอำ" = "approve").

## Workflow per sticker

1. I save the ChatGPT prompt as a file in `mangkorn/prompts/NN-name.md` and push it; the user tells ChatGPT to use that file; the user attaches the references; ChatGPT makes the image; the user attaches it in the Claude chat and I save it to `mangkorn/incoming/NN-name.png`. Pure green (#00FF00) background, no text.
2. I remove the green, trim, and fit it into 370×320 with a 10 px margin (even width and height), then send a preview.
3. User approves → saved as `mangkorn/stickers/NN-name.png`.
4. At the end: main image (240×240), tab image (96×74), validation, ZIP.

## LINE sticker rules (official guideline: https://creator.line.me/en/guideline/sticker/)

- 8 / 16 / 24 / 32 / 40 stickers per set.
- Each sticker: PNG, max 370×320 px, even width and height, ≤ 1 MB, transparent background, about 10 px margin, RGB, ≥ 72 dpi.
- Main image 240×240, chat tab image 96×74 (each ≤ 1 MB).
- ZIP ≤ 60 MB.

## References

- In this repo, `mangkorn/references/`: `dragon-fighting.png` (main design reference), `dragon-hungry.png`, `dragon-sleeping-zzz.png`, `mx-hug-doll.png` (Mx doll for the Hug sticker). Copied from team-kpi-dashboard `line-stickers/full-res/07–09.png` and `animated-emoji/16-hug/kling-start.png`.
- Eye colours (sampled): MawKorn amber `#FAB311` (gradient `#D11D04` → `#F05D13` → `#FAB311` → `#FDE73D`); Mx blue `#3B9FF5` (gradient `#1A1C72` → `#1D49B9` → `#3B9FF5` → `#90E3FD`).
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
