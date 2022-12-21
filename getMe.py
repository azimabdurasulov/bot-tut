import requests

TOKEN = '5888802954:AAG1jeTE-CAQD2H7hFRje-CH9Yj_Yd6I7_o'

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

if response.status_code == 200:
    data = response.json()
    updates = data['result']
    for update in updates:
        msg = update['message']
        text = msg['text']
        user = msg['from']
        print(user)
