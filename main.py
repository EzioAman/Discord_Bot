import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "⚡ FREAKY NATION // COMMAND CENTER",
        "description": (
            "**WELCOME TO THE ARENA**\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🕹️ **Server Owner**\n"
            "👑 **freaky Pookie**\n\n"
            "🛡️ **Admins**\n"
            "• Depressed Admin\n\n"
            "⚔️ **Elite Members**\n"
            "• Depressed freak\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "**Hardcore Gamer • Anime • Freaky**"
        ),
        "color": 0x00E5FF,
        "thumbnail": {
            "url": "https://i.imgur.com/9Xnt8YJ.png"
        },
        "footer": {
            "text": "FREAKY SYSTEM ONLINE"
        }
    }

    payload = {
        "username": "FREAKY SYSTEM",
        "avatar_url": "https://i.imgur.com/1X4Yk8P.png",
        "embeds": [embed],
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "📜 RULES",
                        "style": 1,
                        "custom_id": "rules"
                    },
                    {
                        "type": 2,
                        "label": "🔥 JOIN THE ARENA",
                        "style": 3,
                        "custom_id": "join"
                    },
                    {
                        "type": 2,
                        "label": "🎯 START MISSION",
                        "style": 2,
                        "custom_id": "mission"
                    }
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    control_panel()
