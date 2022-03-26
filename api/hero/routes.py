from flask import make_response, jsonify, redirect, url_for, Blueprint
from .utils import add_all_ow_heroes
from api.hero.models import Hero

hero = Blueprint('hero', __name__, url_prefix='/hero')

@hero.post('/add_heroes')
def add_heroes() :
    add_all_ow_heroes()

@hero.get('/view_heroes')
def view_heroes() :
    heroes = Hero.query.all()
    return make_response(jsonify(heroes),200)