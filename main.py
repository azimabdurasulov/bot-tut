import os
import requests
TOKEN = os.environ["TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
data = requests.get(url)
print(data.json())