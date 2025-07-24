from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "ТВОЙ_ТОКЕН_БОТА"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/', methods=["GET"])
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        send_message(chat_id, f"Ты сказал: {text}")
    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
