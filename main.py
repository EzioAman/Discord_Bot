import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

WIDTH, HEIGHT = 900, 550

ASSET_VIDEO = "assets/Freaky_nation_GIF.mov"
HUD_IMAGE = "hud.png"
OUTPUT_VIDEO = "final.mp4"

def build_hud():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

    draw.rectangle([0, 0, WIDTH, HEIGHT], outline=(0,255,255,255), width=4)

    draw.text((40, 25), "⚡ FREAKY NATION — NEURAL COMMAND", fill=(0,255,255,255), font=font_title)

    y = 100
    lines = [
        "[ CORE STATUS : ONLINE ]",
        "",
        "👑 COMMANDER   freaky Pookie",
        "🛡 ADMIN CORE  Depressed Admin",
        "⚔ ELITE OPS   Depressed freak",
        "",
        "MODE   : HARDCORE GAMER",
        "STYLE  : ANIME x FREAK",
        "STATUS : LIVE",
        "",
        "Neural grid synchronized...",
        "Battle authority confirmed.",
        "Reality interface engaged."
    ]

    for line in lines:
        draw.text((60, y), line, fill=(200,255,255,255), font=font)
        y += 32

    img.save(HUD_IMAGE)

def build_video():
    subprocess.run([
        "ffmpeg", "-y",
        "-i", ASSET_VIDEO,
        "-i", HUD_IMAGE,
        "-filter_complex",
        "[0:v]scale=900:550[bg];[bg][1:v]overlay=0:0",
        "-pix_fmt", "yuv420p",
        OUTPUT_VIDEO
    ], check=True)

def post_to_discord():
    with open(OUTPUT_VIDEO, "rb") as f:
        r = requests.post(
            WEBHOOK,
            files={"file": ("freaky.mp4", f)},
            data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
        )
        if r.status_code not in [200, 204]:
            print("Failed:", r.text)

if __name__ == "__main__":
    build_hud()
    build_video()
    post_to_discord()
