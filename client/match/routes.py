from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, logout_user
from api.map.models import Map
from api.hero.models import Hero, HeroRole

match = Blueprint('match', __name__, url_prefix='/match')

@match.get('/create')
@login_required
def get_create_match_page():
    ow_maps = Map.query.all()
    ow_heroes = Hero.query.all()
    ow_hero_roles = HeroRole.query.all()
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles)