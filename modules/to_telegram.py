import os
from dotenv import load_dotenv
import requests

load_dotenv()

TG_KEY = os.getenv('TG_ALARM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def msg_to_telegram(msg):
    url = f'https://api.telegram.org/bot{TG_KEY}/sendMessage'
    print("-->",msg)
    params = {'chat_id': os.getenv('CHAT_ID'), 'text': msg}
    requests.get(url, params=params)


# if __name__ == '__main__':
#     msg_to_telegram(msg='This is a test message.')