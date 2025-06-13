import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'po_shaurme1.settings')
django.setup()

from django.conf import settings

def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    token = settings.TELEGRAM_BOT_TOKEN
    updates = get_updates(token)
    print(updates)
