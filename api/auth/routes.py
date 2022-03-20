from flask import request, flash, Flask, session, make_response, jsonify, render_template, redirect, url_for, Blueprint
from flask_login import chec
from werkzeug.security import check_password_hash
from flask_bootstrap import Bootstrap
import pymysql, pyotp, enum
from flask_migrate import Migrate
from dataclasses import dataclass
from forms import LoginForm
from sqlalchemy import Enum, select
from secret import DB_USERNAME, DB_PASSWORD, DB_URI, DB_SCHEMA, SECRET_KEY
from api.user.models import User 

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.post('/login')
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter(User.email==email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return 'NOT LOGGED IN' # if the user doesn't exist or password is wrong, reload the page
    return 'LOGGED IN'