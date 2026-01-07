import os
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")
GIF_PATH = "ui/assets/test.gif"

with open(GIF_PATH, "rb") as f:
    r = requests.post(
        WEBHOOK,
        files={"file": ("test.gif", f)},
        data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
    )

if r.status_code not in (200, 204):
    print("Failed:", r.text)
