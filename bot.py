#TELEGRAM BOT FOR CHECKING CURRENT BITCOIN PRICE
import requests
import misc
from yobit import get_btc
from time import sleep

token = misc.token

# https://api.telegram.org/bot493879616:AAH-gRzzzo4d6XETtGDZ-kink6yMU_KRYmc/sendmessage?chat_id=216052979&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'

global recent_update_id
recent_update_id = 0



def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    
    #Respond only to new messages
    #To get update_id for every updating
    #To write it in the variable and then compare it with last update_id from result list
    
    data = get_updates()
    
    recent_object = data['result'][-1]
    current_update_id = recent_object['update_id']
    
    global recent_update_id
    if recent_update_id != current_update_id: 
        recent_update_id = current_update_id
        chat_id = recent_object['message']['chat']['id']
        m_text = recent_object['message']['text']
        
        message = {'chat_id': chat_id,
               'm_text': m_text}
        return message
    return None


def send_message(chat_id, m_text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&m_text={}'.format(chat_id, m_text)
    requests.get(url)

def main():
    # d = get_updates()
    
    while True:
        answer = get_message()
        
        if answer != None:
            chat_id = answer['chat_id']
            m_text = answer['m_text']
            
            if m_text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue
            
        sleep(2)


if __name__ == '__main__':
    main()