from flask import Flask, request, flash, session, make_response, jsonify, render_template, redirect, url_for, Blueprint
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
import pymysql, pyotp, enum
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from forms import LoginForm
from secret import DB_USERNAME, DB_PASSWORD, DB_URI, DB_SCHEMA, SECRET_KEY

from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(DB_USERNAME,DB_PASSWORD,DB_URI,DB_SCHEMA)

login_manager = LoginManager()

app = Flask(__name__, template_folder='static/templates')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from api.user.models import User
from api.routes import api

'''
SET ENVIRONMENT AS DEVELOPMENT IN POWERSHELL:
    $env:FLASK_ENV = "development"
    flask run


HOW TO LOOK UP CONSTRAINT NAMES:

METHOD 1:
select *
from information_schema.table_constraints
where constraint_schema = 'owdb';

METHOD 2:
select COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_COLUMN_NAME, REFERENCED_TABLE_NAME
from information_schema.KEY_COLUMN_USAGE
where TABLE_NAME = 'user';

Flask-Migrate only gets changes in columns but not for Table Create/Deletions
'''

login_manager.init_app(app)
app.register_blueprint(api)
db.create_all()     

@app.route('/dashboard')
@login_required
def user_dashboard():
    session['name'] = "TESTING"
    return render_template('home/dashboard.html')



@app.get('/login')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/login/2fa")
def get_login_2fa():
    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("accounts/login_2fa.html", secret=secret)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login'))

if __name__ == '__main__':
    app.run( debug = True)