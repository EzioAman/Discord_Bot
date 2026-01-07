import os
import requests
from datetime import datetime

WEBHOOK = os.getenv("WEBHOOK_URL")
MODE = os.getenv("MODE", "HYPE")

now = datetime.now().strftime("%A %I:%M %p")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    if r.status_code not in (200, 204):
        print("Failed:", r.text)

# ================== CONTENT ==================

if MODE == "HYPE":
    embed = {
        "title": "🔥 FREAKY NATION HYPE",
        "description": f"**{now}** — Drop your best clip. Only **FREAKY**.",
        "color": 0x00FFFF
    }

elif MODE == "RULES":
    embed = {
        "title": "📜 FREAKY RULEBOOK",
        "description": (
            "🎮 **Play hard. Respect harder.**\n\n"
            "• No toxicity\n"
            "• No spam\n"
            "• Respect staff\n"
            "• Post only peak clips\n"
            "• No leaks / NSFW\n\n"
            "🌀 *Stay freaky. Stay legendary.*"
        ),
        "color": 0x00FFFF
    }

elif MODE == "STAFF":
    embed = {
        "title": "👑 FREAKY COMMAND CENTER",
        "description": (
            "**Server Owner:** freaky Pookie\n\n"
            "**Admins:** Depressed Admin\n\n"
            "**Elite Members:** Depressed freak\n\n"
            "⚡ *These legends keep Freaky Nation alive.*"
        ),
        "color": 0x00FFFF
    }

else:
    embed = {
        "title": "⚠️ Unknown Mode",
        "description": MODE,
        "color": 0xFF0000
    }

payload = {
    "username": "FREAKY FEED",
    "avatar_url": "https://i.imgur.com/7YQ8F4G.png",
    "embeds": [embed]
}

send(payload)
