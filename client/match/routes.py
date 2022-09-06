from urllib import request
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from api.map.models import Map
from api.hero.models import Hero, HeroRole
from api.match.models import Match, MatchUser, MatchUserHero, Hero
from api.match.forms import CreateMatchForm
import api.user.utils as user_utils
from app import db
from sqlalchemy.orm import joinedload
from api.user.models import User
from sqlalchemy import and_

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
def get_view_match_page(match_id):
    ow_maps = Map.query.all()
    ow_heroes = Hero.query.all()
    ow_hero_roles = HeroRole.query.all()
    form = CreateMatchForm()
    match = Match.query.join(MatchUser, Match.users)\
                       .filter(and_(Match.id==match_id, MatchUser.user_id==current_user.id, MatchUser.accepted_flag==True))\
                       .first_or_404()
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles, form=form)

@match.get('/<int:match_id>/edit')
@login_required
def get_edit_match_page(match_id):
    ow_maps = Map.query.all()
    ow_heroes = Hero.query.all()
    ow_hero_roles = HeroRole.query.all()
    form = CreateMatchForm()
    match = Match.query.join(MatchUser, Match.users)\
                       .filter(and_(Match.id==match_id, MatchUser.user_id==current_user.id, MatchUser.accepted_flag==True))\
                       .first_or_404()
    return render_template('match/create_match.html', ow_maps=ow_maps, ow_heroes=ow_heroes, ow_hero_roles=ow_hero_roles, form=form)

@match.get('/all')
@login_required
def get_all_matches_page():
    #current_user_matches = Match.query.filter(MatchUser.user_id==current_user.id).all()
    #current_user_matches = Match.query.join(MatchUser, Match.users).filter(MatchUser.user_id==current_user.id).all()
    results = db.session.query(Match.id, Map.name, Match.match_result, Match.ranked_flag, Match.date_match_played, User.username, HeroRole.title)\
                        .join(MatchUser, Match.users)\
                        .join(Map, Match.map_played)\
                        .join(User, Match.created_by_user)\
                        .join(HeroRole, MatchUser.hero_role)\
                        .filter(MatchUser.user_id==current_user.id)\
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

    return render_template('match/all_matches.html', current_user_matches=[], all_matches=matches)

@match.get('/invites')
@login_required
def get_invited_matches_page():
    # #current_user_matches = Match.query.filter(MatchUser.user_id==current_user.id).all()
    # #current_user_matches = Match.query.join(MatchUser, Match.users).filter(MatchUser.user_id==current_user.id).all()
    # results = db.session.query(Match.id, Map.name, Match.match_result, Match.ranked_flag, Match.date_match_played, User.username)\
    #                     .join(MatchUser, Match.users)\
    #                     .join(Map, Match.map_played)\
    #                     .join(User, Match.created_by_user)\
    #                     .filter(MatchUser.user_id==current_user.id)\
    #                     .all()
    # matches = [] 
    # for match_id, map_name, match_result, ranked_flag, date_match_played, submitted_by_username in results:
    #     matches.append({
    #         "match_id" : match_id,
    #         "map_name" : map_name,
    #         "match_result" : match_result,
    #         "ranked_flag" : ranked_flag,
    #         "date_match_played" : date_match_played,
    #         "submitted_by_username" : submitted_by_username
    #     })
    # print(matches)

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