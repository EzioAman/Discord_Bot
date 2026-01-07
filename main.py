import requests
import os

WEBHOOK = os.environ["WEBHOOK_URL"]

def send(payload):
    requests.post(WEBHOOK, json=payload)

def hype():
    send({
        "username": "FREAKY FEED",
        "content": "🔥 Drop your best clip. Only FREAKY."
    })

def rules():
    send({
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
            "color": 5814784,
            "image": {"url": "https://media.giphy.com/media/QpVUMRUJGokfqXyfa1/giphy.gif"},
            "footer": {"text": "Enter. Perform. Be FREAKY."}
        }]
    })

def staff():
    send({
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
            "color": 5814784,
            "image": {"url": "https://media.giphy.com/media/xTiTnBMEz7zAKs57LG/giphy.gif"},
            "footer": {"text": "Only the Freakiest survive."}
        }]
    })

MODE = os.environ["MODE"]

if MODE == "HYPE":
    hype()
elif MODE == "RULES":
    rules()
elif MODE == "STAFF":
    staff()
