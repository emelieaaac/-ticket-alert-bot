import requests

BOT_TOKEN = "8854359870:AAFUM6dKVVPZZqLSHOxOLHwgufWwtjgGkX0"

CHAT_ID = "8933540965"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {

    "chat_id": CHAT_ID,

    "text": "✅ Test bericht: Telegram werkt!"

}

r = requests.post(url, data=data)

print(r.status_code)

print(r.text)
