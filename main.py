import os
from PIL import Image, ImageDraw, ImageFont
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

WIDTH, HEIGHT = 900, 550


def build_hud():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (10, 12, 18, 255))
    draw = ImageDraw.Draw(img)

    title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    body  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

    # Frame
    draw.rectangle([0, 0, WIDTH, HEIGHT], outline=(0,255,255,255), width=4)

    # Header
    draw.text((40, 20), "⚡ FREAKY NATION — COMMAND CENTER", (0,255,255), font=title)
    draw.rectangle([40, 65, 520, 100], fill=(15, 20, 30, 220))
    draw.text((60, 72), "[  SYSTEM CORE ONLINE  ]", (120,200,255), font=body)

    # Welcome
    draw.text((40, 120), "🔷 WELCOME TO THE BATTLEFIELD", (200,255,255), font=body)
    draw.line((40, 150, 520, 150), fill=(120,255,255), width=2)

    # Personnel
    y = 170
    personnel = [
        ("👑  COMMANDER", "freaky Pookie"),
        ("🛡  ADMIN CORE", "Depressed Admin"),
        ("⚔  ELITE OPERATORS", "Depressed freak")
    ]

    for role, name in personnel:
        draw.text((40, y), role, (255,255,255), font=body)
        draw.text((280, y), name, (180,220,255), font=body)
        y += 40

    # Divider
    y += 10
    draw.line((40, y, 520, y), fill=(120,255,255), width=2)

    # Status
    y += 20
    stats = [
        "🎮 MODE : HARDCORE GAMER",
        "🧬 STYLE : ANIME × FREAK",
        "🟦 STATUS : LIVE",
        "",
        "🌀 The system watches every move...",
        "FREAKY SYSTEM • NEURAL INTERFACE ACTIVE"
    ]

    for line in stats:
        draw.text((40, y), line, (200,255,255), font=small)
        y += 28

    path = "hud.png"
    img.save(path)
    return path


def post_to_discord(image_path):
    with open(image_path, "rb") as f:
        requests.post(
            WEBHOOK,
            files={"file": ("hud.png", f)},
            data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
        )


if __name__ == "__main__":
    hud = build_hud()
    post_to_discord(hud)
