import os
import requests
import subprocess

WEBHOOK = os.environ["WEBHOOK_URL"]

subprocess.run(["python", "ui/render.py"])

with open("panel.png", "rb") as f:
    requests.post(WEBHOOK, files={"file": f})
