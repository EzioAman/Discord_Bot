import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():
    embed = {
        "title": "⚡ FREAKY NATION",
        "description": (
            "**WELCOME TO THE BATTLEFIELD**\n\n"
            "👑 **Pookie**\n"
            "🛡️ *Depressed Admin*\n"
            "⚔️ *Depressed freak*\n\n"
            "🎮 **Hardcore Gamer**  •  🧠 **Anime**  •  🔥 **Freaky**"
        ),
        "color": 0x00F6FF,
        "image": {
            "url": "https://media.tenor.com/1KkZp2-2NfIAAAAC/anime-glitch.gif"
        },
        "thumbnail": {
            "url": "https://media.tenor.com/Wn9n4QZC1tYAAAAC/anime-hud.gif"
        },
        "footer": {
            "text": "FREAKY SYSTEM ONLINE"
        }
    }

    payload = {
        "username": "FREAKY SYSTEM",
        "avatar_url": "https://i.imgur.com/1Xb8nCk.gif",
        "embeds": [embed],
        "components": [
            {
                "type": 1,
                "components": [
                    {"type": 2, "label": "ENTER", "style": 3, "custom_id": "enter"},
                    {"type": 2, "label": "RULES", "style": 1, "custom_id": "rules"},
                    {"type": 2, "label": "ROSTER", "style": 2, "custom_id": "roster"}
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    control_panel()
