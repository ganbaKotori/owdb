from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, logout_user
from api.auth.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.get('/login')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.get('/register')
def register() :
    return render_template('register.html')