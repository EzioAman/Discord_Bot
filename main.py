import os, requests

WEBHOOK = os.getenv("WEBHOOK_URL")

def send(payload):
    r = requests.post(WEBHOOK, json=payload)
    print("Status:", r.status_code)

def control_panel():

    embed = {
        "title": "⚡ FREAKY NATION — COMMAND CENTER",
        "description": (
            "```ansi\n"
            "\u001b[1;34m[ SYSTEM ONLINE ]\u001b[0m\n"
            "\u001b[1;36mWELCOME TO THE BATTLEFIELD\u001b[0m\n"
            "```\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"

            "👑 **COMMANDER**\n"
            "▸ **freaky Pookie**\n\n"

            "🛡️ **ADMIN CORE**\n"
            "▸ Depressed Admin\n\n"

            "⚔️ **ELITE OPERATORS**\n"
            "▸ Depressed freak\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎮 **MODE:** Hardcore Gamer\n"
            "🧠 **STYLE:** Anime / Freak\n"
            "🟦 **STATUS:** `LIVE`"
        ),
        "color": 0x00BFFF,
        "footer": {
            "text": "FREAKY SYSTEM — REALTIME CONTROL INTERFACE"
        }
    }

    payload = {
        "username": "FREAKY SYSTEM",
        "avatar_url": "https://i.imgur.com/8Km9tLL.png",
        "embeds": [embed],
        "components": [
            {
                "type": 1,
                "components": [
                    {"type": 2, "label": "🎯 START MISSION", "style": 3, "custom_id": "start"},
                    {"type": 2, "label": "📜 RULEBOOK", "style": 1, "custom_id": "rules"},
                    {"type": 2, "label": "🧬 PLAYER STATS", "style": 2, "custom_id": "stats"},
                    {"type": 2, "label": "🔥 JOIN BATTLE", "style": 4, "custom_id": "join"}
                ]
            }
        ]
    }

    send(payload)

if __name__ == "__main__":
    control_panel()
