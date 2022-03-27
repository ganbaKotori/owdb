from flask import make_response, jsonify, redirect, url_for, Blueprint, flash
from api.hero.models import Hero
from api.hero.utils import add_all_ow_heroes

hero = Blueprint('hero', __name__, url_prefix='/hero')

@hero.get('/view_heroes')
def view_heroes() :
    add_all_ow_heroes() 
    heroes = Hero.query.all()
    return make_response(jsonify(heroes),200)