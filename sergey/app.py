from flask import Flask, render_template  # из фласка импортируем класс(Flask)

app = Flask(__name__)  # делаем экземпляр класса

@app.route("/")  # c помощью декоратора @app делаем зрительный образ, то что должно показывать на главной странице
def index():
    user_name = 'Сергей'
    return render_template('index.html', user_name=user_name)

@app.route("/test")  # c помощью декоратора @app делаем зрительный образ, то что должно показывать странице
def test():
    return render_template('test.html')
