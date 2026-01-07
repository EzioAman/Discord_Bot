import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "🔷 FREAKY NATION — GAMER HUB",
        "description": (
            "```ansi\n"
            "\u001b[1;36mWELCOME TO THE BATTLEFIELD\u001b[0m\n"
            "```\n"
            "**━━━━━━━━━━━━━━━━━━━━━━**\n\n"
            "👑 **SERVER OWNER**\n"
            "> **freaky Pookie**\n\n"
            "🛡️ **ADMIN CORE**\n"
            "> Depressed Admin\n\n"
            "⚔️ **ELITE OPERATORS**\n"
            "> Depressed freak\n\n"
            "**━━━━━━━━━━━━━━━━━━━━━━**\n"
            "🎮 *Hardcore Gamer • Anime • Freaky*\n\n"
            "🟦 **SYSTEM STATUS:** `ONLINE`"
        ),
        "color": 0x00C8FF,
        "footer": {
            "text": "FREAKY SYSTEM — LIVE CONTROL"
        }
    }

    payload = {
        "username": "FREAKY SYSTEM",
        "avatar_url": "https://cdn.discordapp.com/attachments/1137710049365461033/1210223244771586048/freaky_core.png",
        "embeds": [embed],
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "📜 RULEBOOK",
                        "style": 1,
                        "custom_id": "rules"
                    },
                    {
                        "type": 2,
                        "label": "🔥 ENTER ARENA",
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
