# 📬 alert.py — Sends a Telegram message using your bot

import requests

# 🔐 Your bot token and chat ID
bot_token = "7904841991:AAFzU9jTtptfYnrnV2ac1dXyZoJW-ozUVXI"
chat_id = "8092631789"

def send_alert(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("[✔] Telegram alert sent!")
        else:
            print("[⚠] Failed to send alert.")
    except:
        print("[❌] Error while sending alert.")
