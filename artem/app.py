from flask import Flask, render_template, request, redirect, url_for  # Импорт из модуля класс Flask, render - передаем шаблон
from form import DemoForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "ghbdtn"


@app.route("/", methods = ['GET', 'POST'])
def index():  # В шаблоне base через url_for передал функции (index/test)
    user_name = 'Artem'  # Передаем в render_template -> передается из контрролера в шаблон index.html
    form = DemoForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html',user_name=user_name,form=form)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/services/<service_name>')
def services(service_name):
    return render_template('service.html', service_name=service_name)


