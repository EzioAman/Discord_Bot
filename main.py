import os
import subprocess
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

gif_path = subprocess.check_output(["python", "ui/composite.py"]).decode().strip()

with open(gif_path, "rb") as f:
    requests.post(
        WEBHOOK,
        files={"file": ("final.gif", f)},
        data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
    )
