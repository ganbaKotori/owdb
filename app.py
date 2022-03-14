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

from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash








conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(DB_USERNAME,DB_PASSWORD,DB_URI,DB_SCHEMA)

login_manager = LoginManager()

app = Flask(__name__)

#$env:FLASK_ENV = "development"
#flask run

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

Bootstrap(app)


from api.user.models import User
login_manager.init_app(app)




totp = pyotp.TOTP("base32secret3232")
print(totp.now())

'''
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


from api.routes import api

app.register_blueprint(api)


class MatchResult(enum.Enum):
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"
    DRAW = "DRAW"

class MatchPhase(enum.Enum):
    ATTACK = "VICTORY"
    DEFEND = "DEFEAT"
    CONTROL = "CONTROL"


@dataclass
class Match(db.Model):
    __tablename__ = "ow_match"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    map_played_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ranked_flag = db.Column(db.Boolean)

    map_played = db.relationship("Map")
    rounds = db.relationship('MatchRound', backref='match')

    result = db.Column(Enum(MatchResult))

@dataclass
class MatchRound(db.Model):
    __tablename__ = "ow_match_round"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))

@dataclass
class HeroRole(db.Model):
    __tablename__ = "ow_hero_role"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    title = db.Column(db.String(25), nullable=False, unique=True)

@dataclass
class Hero(db.Model):
    __tablename__ = "ow_hero"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))
    hero_role = db.relationship("HeroRole")

@dataclass
class Map(db.Model):
    __tablename__ = "ow_map"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    map_mode_id = db.Column(db.Integer, db.ForeignKey('ow_map_mode.id'))
    map_mode = db.relationship("MapMode")

    map_stages = db.relationship('MapStage', backref='ow_map')

@dataclass
class MapMode(db.Model):
    __tablename__ = "ow_map_mode"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))

@dataclass
class MapStage(db.Model):
    __tablename__ = "ow_match_stage"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    ow_map_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))





db.create_all()     

@app.route('/')
def index():
    session['name'] = "TESTING"
    return '<h1>OWDB Home Page</h1>'

@app.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('home/dashboard.html')

@app.route('/register')
def register():
    name = session['name']
    print(name)
    return '<h1>OWDB Home Page</h1>'

@app.get('/login')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/login/2fa")
def get_login_2fa():
    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("accounts/login_2fa.html", secret=secret)

@app.post('/login')
def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        login_data = form.data
        user = User.query.filter(User.username == login_data["username"]).first()
        if not user:
            return 'NO USER FOUND'
        login_user(user)
    else: return "FILL IN ALL THE FIELDS"
    return redirect(url_for('user_dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login'))

if __name__ == '__main__':
    app.run( debug = True)