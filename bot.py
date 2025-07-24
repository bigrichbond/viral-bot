from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '8360849754:AAGndHIvG7cyg_RlDOJj2gv_49Gw0Bq2g5U'
TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}'

# Отправка текстового сообщения
def send_message(chat_id, text, reply_markup=None):
    data = {'chat_id': chat_id, 'text': text}
    if reply_markup:
        data['reply_markup'] = reply_markup
    requests.post(f'{TELEGRAM_API}/sendMessage', json=data)

# Отправка фото
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
            buttons = {
                'keyboard': [[{'text': '📸 Фото'}, {'text': '❓ Справка'}]],
                'resize_keyboard': True
            }
            send_message(chat_id, 'Привет! Выбери действие:', reply_markup=buttons)

        elif text == '📸 Фото':
            photo_url = 'https://placekitten.com/400/300'
            send_photo(chat_id, photo_url, 'Вот тебе котик 🐱')

        elif text == '❓ Справка':
            send_message(chat_id, 'Я тестовый бот. Напиши что угодно, и я повторю.')

        else:
            send_message(chat_id, f'Ты сказал: {text}')

    return {'ok': True}

@app.route('/')
def home():
    return 'Bot is running with buttons and photo support.'

if __name__ == '__main__':
    app.run()
