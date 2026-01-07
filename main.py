import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "⚡ 𝙵𝚁𝙴𝙰𝙺𝚈 𝙽𝙰𝚃𝙸𝙾𝙽 — 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙲𝙴𝙽𝚃𝙴𝚁",
        "description": (
            "```fix\n"
            "[ SYSTEM CORE ONLINE ]\n"
            "```\n"
            "**💠 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚃𝙷𝙴 𝙱𝙰𝚃𝚃𝙻𝙴𝙵𝙸𝙴𝙻𝙳**\n\n"

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

            "🌀 *The system watches every move…*"
        ),
        "color": 0x00E5FF,
        "thumbnail": {
            "url": "https://media.tenor.com/2roX3uxz_68AAAAC/anime-power.gif"
        },
        "image": {
            "url": "https://media.tenor.com/f9XK8C5ZzE4AAAAC/anime-glitch.gif"
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
