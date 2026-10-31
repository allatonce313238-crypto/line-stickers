# Rules for every MawKorn sticker prompt

Attach: `mangkorn/references/attach-stickers.png` (top: identity sheet, bottom: sticker pose sheet). Same image for every sticker; in the same ChatGPT chat attach it once.

Every sticker prompt ends with this block:

```
Character: Mangkorn, the chibi red dragon in the attached reference sheets. Keep his design IDENTICAL: cat-like face, amber eyes, small fangs, rosy cheeks, dark brown horns with gold bands, gold crown with a red gem, red scales with gold diamond studs, cream fluffy fur on ears, cheeks, chest and tail, dark brown hand paws, pink-padded feet, red wings with gold edges.
Style: the same 16-bit pixel art with bold dark outlines, bright saturated colors, cute chibi proportions.
Output: ONE single sticker image, square 1:1, the character alone, full body, centered, with empty space around him on every side.
Background: solid flat pure green (#00FF00) everywhere, no shadow, no floor, no gradient. Do not use any green on the character or effects.
NO white border or sticker outline around him. NO text, NO letters, NO speech bubbles. NO tears.
Eyes: big OPEN round amber eyes with white shine, unless this prompt says otherwise. NEVER use squeezed "> <" eyes or closed-curve eyes unless this prompt asks for them.
Do NOT copy the pose, angle or layout of any earlier sticker in this chat: follow only the pose written above.
```

Never put the sticker name in quotes in the prompt (e.g. "Hello"): ChatGPT then writes it as text. Describe the meaning instead.

## Processing (Claude)

`python3 tools/make_sticker.py mangkorn/incoming/NN-name-vN.png mangkorn/stickers/NN-name.png [--drop x0,y0,x1,y1]`
removes green + white border, drops unwanted text pieces inside the box, fits into 370×320 with a 10 px margin.
Add `--no-border` when ChatGPT drew NO white border: otherwise white fur/plates touching the green get erased.

Effects must not be white (white touching the green is removed with the border). Use yellow, orange or red effects.

Proportions: match the reference sheets (head about half of total height, round body with visible cream chest, short visible legs). Never say "head as big as the whole body": it makes him too short.

Facing: draw him facing the viewer (front view, or 3/4 with the face and eyes turned toward the viewer), like a character that looks at whoever reads the chat. Do not draw a pure side view unless the pose needs it.
