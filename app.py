from flask import Flask, session, make_response, jsonify, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
from flask_bootstrap import Bootstrap
import pymysql, pyotp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from forms import LoginForm
from secret import DB_USERNAME, DB_PASSWORD, DB_URI, DB_SCHEMA, SECRET_KEY

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

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

@dataclass
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id : int
    email : str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(12), unique=True)

    ranked_matches = db.relationship('RankedMatch', backref='original_user')

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

@dataclass
class Map(db.Model):
    __tablename__ = "ow_map"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))

@dataclass
class MapMode(db.Model):
    __tablename__ = "ow_map_mode"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))

@dataclass
class RankedMatch(db.Model):
    __tablename__ = "ranked_match"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    map_played_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))
    map_played = db.relationship("Map")

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

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

@app.route('/users')
def get_users():
    users = User.query.all()
    return make_response(jsonify(users),200)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login'))

if __name__ == '__main__':
    app.run( debug = True)