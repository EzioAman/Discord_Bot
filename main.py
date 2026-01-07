import os
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")
MODE = os.getenv("MODE", "TEST")

if not WEBHOOK:
    print("❌ WEBHOOK_URL missing")
    exit(1)

def send(msg):
    r = requests.post(WEBHOOK, json={"content": msg})
    print("Status:", r.status_code)
    print("Response:", r.text)

if MODE == "HYPE":
    send("🔥 **FREAKY HYPE** — Drop your best clip. Only FREAKY.")

elif MODE == "RULES":
    send("📜 **SERVER RULES** — Respect. No toxicity. Stay freaky.")

elif MODE == "STAFF":
    send("👑 **SERVER STAFF**\nOwner: Pookie\nAdmins: Depressed Admin\nImportant: Depressed Freak")

else:
    send("🧪 Test message from GitHub Actions.")
