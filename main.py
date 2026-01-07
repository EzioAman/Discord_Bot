import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

WIDTH, HEIGHT = 900, 550
VIDEO = "assets/Freaky_nation_GIF.mov"
GIF_BG = "bg.gif"
FINAL = "final.gif"


def convert_video_to_gif():
    subprocess.run([
        "ffmpeg", "-y", "-i", VIDEO,
        "-vf", "scale=900:300:flags=lanczos",
        GIF_BG
    ], check=True)


def build_hud_overlay():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (10, 12, 18, 230))
    draw = ImageDraw.Draw(img)

    title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    body  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

    draw.rectangle([0, 0, WIDTH, HEIGHT], outline=(0,255,255,255), width=4)
    draw.text((30, 20), "⚡ FREAKY NATION — COMMAND CENTER", (0,255,255), font=title)
    draw.rectangle([30, 65, 520, 100], fill=(15, 20, 30, 200))
    draw.text((50, 72), "[  SYSTEM CORE ONLINE  ]", (120,200,255), font=body)

    y = 120
    lines = [
        "▣ WELCOME TO THE BATTLEFIELD",
        "",
        "👑 COMMANDER        freaky Pookie",
        "🛡 ADMIN CORE       Depressed Admin",
        "⚔ ELITE OPERATORS   Depressed freak",
        "",
        "MODE   : HARDCORE GAMER",
        "STYLE  : ANIME × FREAK",
        "STATUS : LIVE",
        "",
        "🌀 The system watches every move...",
        "FREAKY SYSTEM • NEURAL INTERFACE ACTIVE"
    ]

    for line in lines:
        draw.text((40, y), line, (200,255,255), font=small)
        y += 28

    return img


def merge_gif_and_hud():
    from PIL import ImageSequence

    overlay = build_hud_overlay()
    frames = []

    bg = Image.open(GIF_BG)
    for frame in ImageSequence.Iterator(bg):
        canvas = Image.new("RGBA", (WIDTH, HEIGHT + 300), (0,0,0,255))
        canvas.paste(overlay, (0,0))
        canvas.paste(frame.convert("RGBA"), (0, HEIGHT))
        frames.append(canvas)

    frames[0].save(
        FINAL, save_all=True,
        append_images=frames[1:],
        loop=0, duration=80
    )


def post_to_discord():
    with open(FINAL, "rb") as f:
        requests.post(
            WEBHOOK,
            files={"file": ("freaky.gif", f)},
            data={"content": "🧠 **FREAKY SYSTEM ONLINE** — Welcome to the arena."}
        )


if __name__ == "__main__":
    convert_video_to_gif()
    merge_gif_and_hud()
    post_to_discord()
