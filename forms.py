from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')

class RegisterForm(FlaskForm) :
    username = StringField('Username')
    password = StringField('Password')
    confirm_password = StringField('Retype Password')