import email
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired


class Demoform(FlaskForm):
    name = StringField('Имя')
    email = EmailField(
        'Email', validators=[DataRequired('Email обязательно для заполнения')]
    )
    submit = SubmitField('Отправить сообщение')
