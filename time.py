from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_datetime():
    # Получаем текущую дату и время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем HTML-код с датой и временем
    return f"<h1>Текущие дата и время:</h1><p>{current_time}</p>"

if __name__ == "__main__":
    # Запускаем приложение
    app.run(debug=True)
