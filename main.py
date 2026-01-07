import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "⚡ FREAKY NATION :: NEURAL COMMAND",
        "description": (
            "```ansi\n"
            "\u001b[1;36m▓▓▓▓▓ CORE STATUS : ONLINE ▓▓▓▓▓\u001b[0m\n"
            "\u001b[2;35mNEURAL LINK ESTABLISHED // SYNC 100%\u001b[0m\n"
            "```"
            "🧬 **WELCOME TO THE ARENA**\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👑 **COMMANDER**\n"
            "➤ **freaky Pookie**\n\n"

            "🛡️ **ADMIN CORE**\n"
            "➤ Depressed Admin\n\n"

            "⚔️ **ELITE OPERATORS**\n"
            "➤ Depressed freak\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎮 **MODE:** `HARDCORE`\n"
            "🧠 **STYLE:** `ANIME × FREAK`\n"
            "🟦 **STATUS:** `LIVE`\n\n"

            "💠 _Neural grid pulsing..._\n"
            "⚠️ _Battle authority confirmed._\n"
            "🧬 _Reality interface engaged._"
        ),
        "color": 0x00F6FF,
        "thumbnail": {
            "url": "https://media.tenor.com/Wn9n4QZC1tYAAAAC/anime-hud.gif"
        },
        "image": {
            "url": "https://media.tenor.com/1KkZp2-2NfIAAAAC/anime-glitch.gif"
        },
        "footer": {
            "text": "FREAKY SYSTEM • NEURAL INTERFACE ACTIVE"
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
                    {"type": 2, "label": "⚔ DEPLOY", "style": 3, "custom_id": "deploy"},
                    {"type": 2, "label": "📜 RULES", "style": 1, "custom_id": "rules"},
                    {"type": 2, "label": "🧬 PROFILE", "style": 2, "custom_id": "profile"},
                    {"type": 2, "label": "🔥 ENTER ARENA", "style": 4, "custom_id": "join"}
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    control_panel()
