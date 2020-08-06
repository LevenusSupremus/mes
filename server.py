#coding: utf-8

from flask import Flask, request, Response

import datetime, time

now = datetime.datetime.now()
app = Flask(__name__)

messages = []

class Bot(): # Bot for chat, type 'bot' in your chat to see message from bot
    def send_message(self, name):
        bot_message = {
            'name': 'Bot', 
            'time': time.time(), 
            'text': f'Hello, {name}, i\'m a Bot!'
            }
        messages.append(bot_message)
        return bot_message

bot = Bot()

@app.route("/send", methods=['POST'])
def send(): # Function that calling for POST request 
            # and add message info to the list 'messages'
    name, text = str(request.json.get('name')), str(request.json.get('text'))
    if not name or not isinstance(name, str) \
    or not text or not isinstance(name, str):
        return Response(status=400)
    message = {
        'name': name, 
        'time': time.time(), 
        'text': text
        }
    messages.append(message)
    if 'бот' in text: # this if statement calling for bot
        bot.send_message(name)
    return message

def filter_by_key(elements, key, threshold): # for filter messages by time
    filtered_elements = []
    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)
    return filtered_elements

@app.route("/messages")
def messages_view(): # return messages at the needed period and show them on the web
    try:
        after = float(request.args['after'])
    except:
        return Response(status=400)
    return {'messages' : filter_by_key(messages, key='time', threshold=after)}

@app.route("/") # start page
def hello():
    return "Hello, World! <a href='/status'>Статус</a>"

def stats(what): # getting stats
    if what == 'user_num':
        users_names = []
        users_names = [message['name'] for message in messages \
                        if message['name'] not in users_names]
        what = len(set(users_names))
        return what


@app.route("/status")
def status(): # page to see stats
    return {
        'status': True,
        'app_name':'Messenger',
        'time': str(now),
        'Num of users': stats('user_num'),
    }


app.run()