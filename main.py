import os
import requests
from datetime import datetime

WEBHOOK = os.getenv("WEBHOOK_URL")
MODE = os.getenv("MODE", "PANEL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def admin_panel():
    embed = {
        "title": "🎮 FREAKY NATION CONTROL PANEL",
        "description": "**Welcome to the arena.**\n\nUse the buttons below.",
        "color": 0x00eaff,
        "fields": [
            {"name": "👑 Owner", "value": "freaky Pookie", "inline": False},
            {"name": "🛡 Admins", "value": "Depressed Admin", "inline": False},
            {"name": "⚔ Elite Members", "value": "Depressed freak", "inline": False}
        ],
        "footer": {"text": "Hardcore Gamer • Anime • Freaky"}
    }

    payload = {
        "username": "FREAKY SYSTEM",
        "embeds": [embed],
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "📜 Server Rules",
                        "style": 1,
                        "custom_id": "rules_btn"
                    },
                    {
                        "type": 2,
                        "label": "🔥 Join the Arena",
                        "style": 3,
                        "custom_id": "join_btn"
                    }
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    admin_panel()
