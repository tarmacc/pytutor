from app import db


class UserSubmit(db.Model):
    """Таблица заполненных демо-форм сайта."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
