import requests, os

url = os.getenv("WEBHOOK_URL")

payload = {
    "username": "FREAKY FEED",
    "content": "🧪 Freaky webhook is now LIVE."
}

r = requests.post(url, json=payload)
print("Status:", r.status_code)
print("Response:", r.text)
