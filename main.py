import requests, os

url = os.getenv("WEBHOOK_URL")

payload = {
    "username": "FREAKY FEED",
    "content": "🧪 Webhook test successful. Freaky system is online."
}

r = requests.post(url, json=payload)
print(r.status_code, r.text)
