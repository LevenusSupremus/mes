#coding: utf-8

import requests
import time, datetime



def pretty_message(message):
    dt = datetime.datetime.fromtimestamp(message['time'])
    dt_str = dt.strftime('%H:%M:%S %Y-%m-%d')
    print(message['name'], dt_str)
    print(message['text'])
    print()
after = 0.0
while True:
    data = requests.get(f'http://127.0.0.1:5000/messages', \
        params = {'after':after}).json()
    for message in data['messages']:
        pretty_message(message)
        after = message['time']
    time.sleep(1)