from PIL import Image, ImageSequence
import os

BASE = os.path.dirname(__file__)

gif_path = os.path.join(BASE, "assets/test.gif")
frame_path = os.path.join(BASE, "assets/frame.png")
out_path = os.path.join(BASE, "assets/final.gif")

bg_gif = Image.open(gif_path)
frame = Image.open(frame_path).convert("RGBA")

frames = []
durations = []

for f in ImageSequence.Iterator(bg_gif):
    f = f.convert("RGBA")

    # Resize frame to match each frame
    resized_frame = frame.resize(f.size, Image.LANCZOS)

    composed = Image.alpha_composite(f, resized_frame)

    frames.append(composed)
    durations.append(bg_gif.info.get("duration", 100))

frames[0].save(
    out_path,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2
)

print(out_path)
