from email import message
from app import db

class UserSubmit(db.Model):
    """Таблица заполненных форм (для БД)."""
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
