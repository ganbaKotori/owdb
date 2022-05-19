from flask import Flask, session, render_template, redirect, url_for
from flask_login import LoginManager, login_required, logout_user
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secret import DB_USERNAME, DB_PASSWORD, DB_URI, DB_SCHEMA, SECRET_KEY
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
from client.routes import client

from api.map.utils import add_all_ow_maps
from api.hero.utils import add_all_ow_heroes

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
app.register_blueprint(client)
db.create_all()  

#add_all_ow_maps()
#add_all_ow_heroes()

if __name__ == '__main__':
    app.run()