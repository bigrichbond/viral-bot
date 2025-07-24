from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = '8360849754:AAGndHIvG7cyg_RlDOJj2gv_49Gw0Bq2rs8'
TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}'

def send_message(chat_id, text, reply_markup=None):
    data = {'chat_id': chat_id, 'text': text}
    if reply_markup:
        data['reply_markup'] = reply_markup
    requests.post(f'{TELEGRAM_API}/sendMessage', json=data)

def send_photo(chat_id, photo_url, caption=None):
    data = {'chat_id': chat_id, 'photo': photo_url}
    if caption:
        data['caption'] = caption
    requests.post(f'{TELEGRAM_API}/sendPhoto', json=data)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        if text == '/start':
            send_message(chat_id, 'Бот запущен успешно ✅')
        else:
            send_message(chat_id, f'Вы написали: {text}')
    return jsonify({'ok': True})

@app.route('/', methods=['GET'])
def index():
    return 'Бот работает', 200
