from flask import Flask, request
import telegram

TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Вы написали: {text}")
    return 'ok'

@app.route('/')
def index():
    return "Бот работает!"

if __name__ == '__main__':
    app.run(port=5000)
