from flask import Flask, render_template  # Импорт из модуля класс Flask, render - передаем шаблон

app = Flask(__name__)


@app.route("/")
def index():  # В шаблоне base через url_for передал функции (index/test)
    user_name = 'Artem'  # Передаем в render_template -> передается из контрролера в шаблон index.html
    return render_template('index.html',user_name=user_name)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/services/<service_name>')
def services(service_name):
    return render_template('service.html', service_name=service_name)


