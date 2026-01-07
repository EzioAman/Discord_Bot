import requests
import time
import os
from datetime import datetime

WEBHOOK = os.environ["WEBHOOK_URL"]

def post(msg):
    requests.post(WEBHOOK, json={
        "username": "FREAKY FEED",
        "content": msg
    })

while True:
    now = datetime.now().strftime("%A %I:%M %p")
    post(f"🔥 {now} — Drop your best clip. Only FREAKY.")
    time.sleep(3600)
