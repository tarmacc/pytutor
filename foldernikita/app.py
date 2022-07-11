import os

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY']='key'
app.config["SQLALZHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("index.j2", form=form)

@app.route('/test')
def test():
    return render_template("test.j2")


@app.route('/elements')
def elements():
    return render_template("elements.j2")
