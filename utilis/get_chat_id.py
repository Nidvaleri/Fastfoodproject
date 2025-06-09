import os
import django
import requests

# Устанавливаем настройки Django, чтобы работать с settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'po_shaurme1.settings')
django.setup()

from django.conf import settings

def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    token = settings.TELEGRAM_BOT_TOKEN  # берём токен из settings.py
    updates = get_updates(token)
    print(updates)
