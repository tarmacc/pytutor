import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    SECRET_KEY="gfhjkm",
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(basedir, 'app.db')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
"""Добавляем базу данных и механизм миграции."""
db = SQLAlchemy(app)
migrate = Migrate(app, db)
