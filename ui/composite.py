from PIL import Image, ImageSequence
import os

BASE = os.path.dirname(__file__)

bg_gif = Image.open(os.path.join(BASE, "assets/test.gif")).convert("RGBA")
frame = Image.open(os.path.join(BASE, "assets/frame.png")).convert("RGBA")

frames = []
durations = []

for i, f in enumerate(ImageSequence.Iterator(bg_gif)):
    f = f.convert("RGBA")
    composed = Image.alpha_composite(f, frame)
    frames.append(composed)
    durations.append(bg_gif.info.get("duration", 100))

out_path = os.path.join(BASE, "assets/final.gif")

frames[0].save(
    out_path,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2
)

print(out_path)
