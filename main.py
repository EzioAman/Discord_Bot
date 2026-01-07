import requests
import os
from datetime import datetime

WEBHOOK = os.environ["WEBHOOK_URL"]

def send(payload):
    requests.post(WEBHOOK, json=payload)

def post_rules_panel():
    payload = {
        "username": "FREAKY FEED",
        "embeds": [
            {
                "title": "🎮 Freaky Nation Rulebook",
                "description": (
                    "**Welcome to Freaky Nation.**\n\n"
                    "🔹 Respect the grind\n"
                    "🔹 No toxic spam\n"
                    "🔹 Keep the vibes freaky\n"
                    "🔹 No leaks / no scams\n"
                    "🔹 Mods have final say\n\n"
                    "⚡ Break the rules → get fried."
                ),
                "image": {
                    "url": "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"
                },
                "color": 16711808,
                "footer": {"text": "Press the button below to open the full rulebook."}
            }
        ],
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 5,
                        "label": "📜 View Full Rules",
                        "url": "https://discord.com/channels/@me"
                    }
                ]
            }
        ]
    }
    send(payload)

def post_staff_panel():
    payload = {
        "username": "FREAKY FEED",
        "embeds": [
            {
                "title": "👑 Freaky Nation Command Center",
                "description": (
                    "**Owner:**\n"
                    "💎 **freaky Pookie**\n\n"
                    "**Admin (Depressed Admin):**\n"
                    "🧠 **freaky Chomu**\n\n"
                    "**Important Members (Depressed freak):**\n"
                    "🔥 freaky Ghost\n"
                    "🔥 freaky Havsi\n"
                    "🔥 freaky Samosa\n"
                    "🔥 freaky ur anus is..."
                ),
                "color": 5793266,
                "footer": {"text": "Only Freaks run this place."}
            }
        ]
    }
    send(payload)

def hourly_message():
    now = datetime.now().strftime("%A %I:%M %p")
    send({
        "username": "FREAKY FEED",
        "content": f"🔥 {now} — Drop your best clip. Only FREAKY."
    })

# Schedule logic
hour = datetime.now().hour

if hour == 12:
    post_rules_panel()
elif hour == 18:
    post_staff_panel()
else:
    hourly_message()
