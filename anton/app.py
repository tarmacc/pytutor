import os

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-nejy$#gi#$s123"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from forms import DemoForm
from models import UserSubmit


@app.route("/", methods=["GET", "POST"])
def index():
    """Показ главной страницы."""
    page_title = "Главная"

    return render_template("index.j2", page_title=page_title)


@app.route("/test")
def test():
    """Показ тестовой страницы."""
    page_title = "Тестовая страница"
    return render_template("test.j2", page_title=page_title)


@app.route("/users")
def users():
    page_title = "Список пользователей, кто заполнил форму"
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", page_title=page_title, users=user_list_db)


@app.route("/thanks")
def thanks():
    page_title = "Спасибо за заполнение формы!"
    return render_template("thanks.j2", page_title=page_title)


@app.route("/form", methods=["GET", "POST"])
def demo_form():
    page_title = "Демо-форма"
    form = DemoForm()
    if form.validate_on_submit():
        print(f"Имя кто заполнил: {request.form.get('name')}, \nEmail: {request.form.get('email')}")
        user_db = UserSubmit(
            name=f"{request.form.get('name')} {request.form.get('last_name')}",
            email=request.form.get('email')
        )
        db.session.add(user_db)
        db.session.commit()

        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email)
        return redirect("thanks")
    return render_template("test-form.j2", page_title=page_title, form=form)
