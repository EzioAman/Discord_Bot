import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "⚡ 𝙵𝚁𝙴𝙰𝙺𝚈 𝙽𝙰𝚃𝙸𝙾𝙽 :: 𝙽𝙴𝚄𝚁𝙰𝙻 𝙲𝙾𝙼𝙼𝙰𝙽𝙳",
        "description": (
            "```ansi\n"
            "\u001b[1;36m[ CORE STATUS : ONLINE ]\u001b[0m\n"
            "```"
            "🧬 **𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚃𝙷𝙴 𝙰𝚁𝙴𝙽𝙰**\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👑 **𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝙴𝚁**\n"
            "▸ **freaky Pookie**\n\n"

            "🛡️ **𝙰𝙳𝙼𝙸𝙽 𝙲𝙾𝚁𝙴**\n"
            "▸ Depressed Admin\n\n"

            "⚔️ **𝙴𝙻𝙸𝚃𝙴 𝙾𝙿𝙴𝚁𝙰𝚃𝙾𝚁𝚂**\n"
            "▸ Depressed freak\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎮 **MODE:** Hardcore Gamer\n"
            "🧠 **STYLE:** Anime × Freak\n"
            "🟦 **STATUS:** `LIVE`\n\n"

            "💠 _Neural systems synchronized..._\n"
            "⚠️ _Battlefield authority confirmed._"
        ),
        "color": 0x00F6FF,
        "thumbnail": {
            "url": "https://media.tenor.com/yoQSSzA8oKcAAAAC/anime-cyber.gif"
        },
        "image": {
            "url": "https://media.tenor.com/Kf6kZ0g6A6wAAAAC/anime-glitch.gif"
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
                    {"type": 2, "label": "📜 CODEX", "style": 1, "custom_id": "rules"},
                    {"type": 2, "label": "🧬 PROFILE", "style": 2, "custom_id": "stats"},
                    {"type": 2, "label": "🔥 ENTER ARENA", "style": 4, "custom_id": "join"}
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    control_panel()
