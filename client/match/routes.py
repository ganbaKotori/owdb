from urllib import request
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from api.map.models import Map
from api.hero.models import Hero, HeroRole
from api.match.models import Match
from api.match.forms import CreateMatchForm
import api.user.utils as user_utils

match = Blueprint('match', __name__, url_prefix='/match')

@match.get('/create')
@login_required
def get_create_match_page():
    ow_maps = Map.query.all()
    ow_heroes = Hero.query.all()
    ow_hero_roles = HeroRole.query.all()
    friends = user_utils.get_current_user_friends()
    print(friends)
    current_user_friends = [(f, f) for f in user_utils.get_current_user_friends()]
    print(current_user_friends)
    form = CreateMatchForm()
    form.tagged_friends[0].username.choices = current_user_friends
    print(form.tagged_friends[0].username)
    print('create match page')
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles, form=form)

@match.get('/<int:match_id>')
@login_required
def get_edit_match_page(match_id):
    ow_maps = Map.query.all()
    ow_heroes = Hero.query.all()
    ow_hero_roles = HeroRole.query.all()
    form = CreateMatchForm()
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles, form=form)

@match.get('/all')
@login_required
def get_all_matches_page():
    current_user_matches = Match.query.filter(Match.created_by_user_id==current_user.id).all()
    return render_template('match/all_matches.html', current_user_matches=current_user_matches)