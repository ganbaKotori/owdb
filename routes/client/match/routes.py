from urllib import request
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from models.map.Map import Map
from models.map.MapMode import MapMode
from models.hero.Hero import Hero
from models.hero.HeroRole import HeroRole
from models.match.Match import Match
from models.match.MatchUser import MatchUser
from routes.api.match.forms import CreateMatchForm
import routes.api.user.utils as user_utils
from app import db
from sqlalchemy.orm import joinedload
from models.user.User import User
from sqlalchemy import and_
import routes.api.match.utils as match_utils
from schema.match.MatchSchema import MatchSchema

from utils.map.utils import get_all_map_json
from utils.hero.utils import get_all_heroes_json

match = Blueprint('match', __name__, url_prefix='/m')

@match.get('/create')
@login_required
def get_create_match_page():
    ow_maps = get_all_map_json()
    ow_heroes = Hero.query.order_by(Hero.name.asc()).all()
    ow_hero_roles = HeroRole.query.all()
    friends = user_utils.get_current_user_friends()
    print(friends)
    current_user_friends = [(f, f) for f in user_utils.get_current_user_friends()]
    print(current_user_friends)
    form = CreateMatchForm()
    # form.tagged_friends[0].username.choices = current_user_friends
    # print(form.tagged_friends[0].username)
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles,form=form,friends=friends)

@match.get('/<int:match_id>')
@login_required
def get_view_match_page(match_id):
    match = Match.query.filter(Match.id==match_id).first_or_404()
    return render_template('match/view_match.html', match=match)

@match.get('/<int:match_id>/edit')
@login_required
def get_edit_match_page(match_id):
    ow_maps = get_all_map_json()
    ow_heroes = get_all_heroes_json()
    ow_hero_roles = HeroRole.query.all()
    ow_map_modes = MapMode.query.order_by().all()
    form = CreateMatchForm()
    match = Match.query.join(MatchUser, Match.users)\
                       .filter(and_(Match.id==match_id, MatchUser.user_id==current_user.id, MatchUser.accepted_flag==True))\
                       .first_or_404()
    match_schema = MatchSchema()
    match_json = match_schema.dump(match)
    
    c_u_match_info = next(user for user in match.users if user.user_id == current_user.id)
    c_u_heroes = [match_hero.hero.id for match_hero in c_u_match_info.heroes_played]
    c_u_hero_role_id = c_u_match_info.hero_role.id
    match_map_id = match.map_played.id
    print(c_u_heroes)
    print(c_u_hero_role_id)#
    
    return render_template('match/edit_match.html',
                            match=match_json,
                            ow_maps=ow_maps,
                            ow_heroes=ow_heroes,
                            ow_hero_roles=ow_hero_roles,
                            ow_map_modes=ow_map_modes,
                            form=form,
                            c_u_heroes=c_u_heroes,
                            c_u_hero_role_id=c_u_hero_role_id,
                            match_map_id=match_map_id,
                            match_json=match_json)


@match.get('/all')
@login_required
def get_all_matches_page():
    all_matches = match_utils.get_current_user_matches(user_id=current_user.id)
    return render_template('match/all_matches.html', current_user_matches=[], all_matches=all_matches)

@match.get('/invites')
@login_required
def get_invited_matches_page():

    results = db.session.query(Match.id, Map.name, Match.match_result, Match.ranked_flag, Match.date_match_played, User.username, HeroRole.title)\
                        .join(MatchUser, Match.users)\
                        .join(Map, Match.map_played)\
                        .join(User, Match.created_by_user)\
                        .join(HeroRole, MatchUser.hero_role)\
                        .filter(MatchUser.user_id==current_user.id)\
                        .filter(MatchUser.accepted_flag==False)\
                        .all()
    matches = [] 
    for match_id, map_name, match_result, ranked_flag, date_match_played, submitted_by_username, hero_role in results:
        matches.append({
            "match_id" : match_id,
            "map_name" : map_name,
            "match_result" : match_result,
            "ranked_flag" : ranked_flag,
            "date_match_played" : date_match_played,
            "submitted_by_username" : submitted_by_username,
            "hero_role" : hero_role
        })
    print(matches)

    return render_template('match/invited_matches.html',match_invites=matches)