import requests
import os
from datetime import datetime, timezone, timedelta

WEBHOOK = os.environ["WEBHOOK_URL"]
NEON = 5814784

IST = timezone(timedelta(hours=5, minutes=30))

def send(payload):
    requests.post(WEBHOOK, json=payload)

def rules_panel():
    payload = {
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "🎮 FREAKY NATION RULEBOOK",
            "description": (
                "⚡ **WELCOME TO THE ARENA** ⚡\n\n"
                "🌀 Respect the grind\n"
                "🚫 No toxic spam\n"
                "💎 Keep the vibes freaky\n"
                "🧠 No leaks • No scams\n"
                "👑 Mods have final say\n\n"
                "🔥 Break the code → Get deleted"
            ),
            "color": NEON,
            "image": {"url": "https://media.giphy.com/media/QpVUMRUJGokfqXyfa1/giphy.gif"},
            "footer": {"text": "Enter. Perform. Be FREAKY."}
        }]
    }
    send(payload)

def staff_panel():
    payload = {
        "username": "FREAKY FEED",
        "embeds": [{
            "title": "👑 FREAKY COMMAND CENTER",
            "description": (
                "💠 **OWNER**\n"
                "💎 freaky Pookie\n\n"
                "🧠 **DEPRESSED ADMIN**\n"
                "⚔️ freaky Chomu\n\n"
                "🔥 **DEPRESSED FREAKS**\n"
                "🌀 freaky Ghost\n"
                "🌀 freaky Havsi\n"
                "🌀 freaky Samosa\n"
                "🌀 freaky ur anus is..."
            ),
            "color": NEON,
            "image": {"url": "https://media.giphy.com/media/xTiTnBMEz7zAKs57LG/giphy.gif"},
            "footer": {"text": "Only the Freakiest survive."}
        }]
    }
    send(payload)

def hype_message():
    now = datetime.now(IST).strftime("%A %I:%M %p")
    send({
        "username": "FREAKY FEED",
        "content": f"🔥 {now} — Drop your best clip. Only FREAKY."
    })

now = datetime.now(IST)
hour = now.hour

if hour == 23:   # 11 PM IST → Rules Panel
    rules_panel()
elif hour == 17: # 5 PM IST → Staff Panel
    staff_panel()
else:
    hype_message()
