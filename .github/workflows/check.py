import requests

url = "https://www.axs.com/events/1141607/ariana-grande-extra-date-added-tickets"

BOT_TOKEN = "8854359870:AAFUM6dKVVPZZqLSHOxOLHwgufWwtjgGkX0"
CHAT_ID = "8933540965"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

r = requests.get(url)
text = r.text.lower()

signals = [
    "choose from the map",
    "pick your tickets",
    "find tickets",
    "buy tickets",
    "select seats"
]

if any(s in text for s in signals):
    send("🚨 AXS TICKETS MOGELIJK BESCHIKBAAR!\n" + url)
    print("sent alert")
else:
    print("no tickets")
