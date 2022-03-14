from flask import Flask, session, make_response, jsonify, render_template, redirect, url_for, Blueprint
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
from flask_bootstrap import Bootstrap
import pymysql, pyotp, enum
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from forms import LoginForm
from sqlalchemy import Enum, select
from secret import DB_USERNAME, DB_PASSWORD, DB_URI, DB_SCHEMA, SECRET_KEY
from api.user.models import User 
user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/users')
def get_users():
    users = User.query.all()
    return make_response(jsonify(users),200)