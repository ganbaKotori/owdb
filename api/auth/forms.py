from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')