"""Turn a ChatGPT sticker image (character on pure green) into a LINE sticker PNG.

Removes the green background and any white die-cut border touching it, drops
pieces inside --drop boxes (e.g. unwanted text), clamps green spill, then fits
the result into 370x320 with a 10 px margin and even width/height.

usage: python3 make_sticker.py IN.png OUT.png [--drop x0,y0,x1,y1 ...]
"""
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage as nd

MAX_W, MAX_H, MARGIN = 370, 320, 10

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('dst')
ap.add_argument('--drop', action='append', default=[], help='x0,y0,x1,y1: remove pieces fully inside this box')
args = ap.parse_args()

im = np.array(Image.open(args.src).convert('RGB')).astype(int)
r, g, b = im[..., 0], im[..., 1], im[..., 2]
green = (g - np.maximum(r, b) > 60) & (g > 150)
white = (r > 215) & (g > 215) & (b > 205)
lab, _ = nd.label(green | white)
bg = np.isin(lab, list(set(np.unique(lab[green])) - {0}))
mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
halo = ((mx - mn < 45) & (mn > 140)) | (g - np.maximum(r, b) > 15)
for _ in range(3):
    bg |= nd.binary_dilation(bg) & halo

fg = ~bg
lab2, n2 = nd.label(fg)
sizes = nd.sum(fg, lab2, range(1, n2 + 1))
boxes = [tuple(map(int, d.split(','))) for d in args.drop]
keep = np.zeros(n2 + 1, bool)
for i, o in enumerate(nd.find_objects(lab2), 1):
    if sizes[i - 1] < 300:
        continue
    y0, y1, x0, x1 = o[0].start, o[0].stop, o[1].start, o[1].stop
    if any(x0 >= a and y0 >= b_ and x1 <= c and y1 <= d for a, b_, c, d in boxes):
        continue
    keep[i] = True
fg = keep[lab2]

out = im.copy()
out[..., 1] = np.minimum(out[..., 1], np.maximum(out[..., 0], out[..., 2]))
img = Image.fromarray(np.dstack([out, fg * 255]).astype('uint8'), 'RGBA')
img = img.crop(img.getbbox())
s = min((MAX_W - 2 * MARGIN) / img.width, (MAX_H - 2 * MARGIN) / img.height)
nw, nh = round(img.width * s), round(img.height * s)
cw, ch = nw + 2 * MARGIN, nh + 2 * MARGIN
cw += cw % 2; ch += ch % 2
canvas = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
canvas.paste(img.resize((nw, nh), Image.LANCZOS), ((cw - nw) // 2, (ch - nh) // 2))
canvas.save(args.dst, optimize=True)
print(args.dst, canvas.size)
