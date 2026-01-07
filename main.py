import os, requests
from datetime import datetime

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print(r.status_code, r.text)

def hype():
    now = datetime.now().strftime("%A %I:%M %p")
    send({
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "🔥 Freaky Nation Update",
            "description": f"**{now}** — Drop your best clip. Only **FREAKY**.",
            "color": 0x00FFFF
        }]
    })

def daily_challenge():
    send({
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "🏆 Daily Challenge",
            "description": "Post your **best gaming clip** today.\nWinner gets bragging rights.",
            "color": 0x00FFFF
        }]
    })

def rules_panel():
    send({
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "📜 Freaky Rulebook",
            "description": (
                "• Respect everyone\n"
                "• No toxicity / no spam\n"
                "• No NSFW\n"
                "• Follow staff instructions\n"
                "• Have fun and stay freaky"
            ),
            "color": 0x00FFFF
        }]
    })

def staff_panel():
    send({
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "👑 Freaky Command Center",
            "description": (
                "**Owner:** freaky Pookie\n\n"
                "**Admins:** Depressed Admin\n\n"
                "**Important Members:** Depressed freak"
            ),
            "color": 0x00FFFF
        }]
    })

MODE = os.getenv("MODE", "HYPE")

if MODE == "HYPE":
    hype()
elif MODE == "DAILY":
    daily_challenge()
elif MODE == "RULES":
    rules_panel()
elif MODE == "STAFF":
    staff_panel()
