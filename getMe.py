import requests

TOKEN = '5568968030:AAEjux10tuYrcU8yrmAIDWSC0i-ZJgwuRLg'

header = "f430c121f8694734bd0b530c6a059ef2"

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def get_lastupdate(updates):
    last_update = updates['result'][-1]
    chat_id = last_update['message']['chat']['id']
    text = last_update['message']['text']
    another_text = text
    
    
    if text in another_text  :
            text_msg = text
        
    else:
            text_msg = 'Qayta harakat qilib kuring!'
    
    message_id = last_update['message']['message_id']
    return chat_id,text,message_id

def send_message(TOKEN,chat_id,text):
    data = {
            'chat_id':chat_id,
            'text':text
        }

    r = requests.post(url = f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=data, headers=header)    

new_message = -1

while True:
    updates = get_updates(TOKEN)
    lastupdate = get_lastupdate(updates)
    chat_id,text,last_message_id = lastupdate

    if new_message != last_message_id:
        send_message(TOKEN,chat_id=chat_id,text=text)
        new_message = last_message_id
