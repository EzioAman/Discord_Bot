import os
import time
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

WIDTH, HEIGHT = 900, 550

def build_hud():
    img = Image.new("RGB", (WIDTH, HEIGHT), (10, 12, 18))
    draw = ImageDraw.Draw(img)

    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

    draw.rectangle([0, 0, WIDTH, HEIGHT], outline=(0,255,255), width=4)

    draw.text((40, 30), "⚡ FREAKY NATION — NEURAL COMMAND", fill=(0, 255, 255), font=font_title)

    y = 110
    lines = [
        "[ CORE STATUS : ONLINE ]",
        "",
        "👑 COMMANDER      freaky Pookie",
        "🛡 ADMIN CORE     Depressed Admin",
        "⚔ ELITE OPS      Depressed freak",
        "",
        "MODE   : HARDCORE GAMER",
        "STYLE  : ANIME x FREAK",
        "STATUS : LIVE",
        "",
        "Neural grid synchronized...",
        "Battle authority confirmed.",
        "Reality interface engaged.",
    ]

    for line in lines:
        draw.text((60, y), line, fill=(200, 255, 255), font=font)
        y += 32

    path = "hud.png"
    img.save(path)
    return path

def post_to_discord(path):
    with open(path, "rb") as f:
        r = requests.post(
            WEBHOOK,
            files={"file": ("hud.png", f)},
            data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
        )
        if r.status_code != 204:
            print("Failed:", r.text)

if __name__ == "__main__":
    image = build_hud()
    post_to_discord(image)
