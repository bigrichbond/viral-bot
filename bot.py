from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Бот запущен успешно!"

if __name__ == "__main__":
    app.run()
