import os
import subprocess
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")

gif_path = subprocess.check_output(["python", "ui/render.py"]).decode().strip()

with open(gif_path, "rb") as f:
    requests.post(
        WEBHOOK,
        files={"file": ("freaky_hud.gif", f)},
        data={"content": "🧠 **FREAKY SYSTEM ONLINE**"}
    )
