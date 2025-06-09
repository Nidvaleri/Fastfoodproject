import requests
from django.conf import settings

def send_telegram_message(message: str, chat_id: str = None):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = chat_id or settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    response = requests.post(url, data=data)
    print("=== TELEGRAM STATUS ===")
    print(response.status_code)
    print("=== TELEGRAM TEXT ===")
    print(response.text)
    print("=== END ===")
    return response
