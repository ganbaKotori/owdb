from flask import Blueprint, request, redirect, url_for, make_response, jsonify
from app import db
from api.match.models import Match, MatchPhase, MatchResult, MatchRound, MatchHero, MatchUser
from api.map.models import Map
from api.hero.models import Hero
from api.user.models import User
from flask_login import current_user, login_required
from api.match.forms import CreateMatchForm
import api.user.utils as user_utils
from datetime import datetime
from sqlalchemy import and_

match = Blueprint('match', __name__, url_prefix='/match')

@match.post('')
@login_required
def add_match():
    print(request.form)
    print(request.form.get('datetime-match-played'))
    form = CreateMatchForm()
    current_user_friends = [(f, f) for f in user_utils.get_current_user_friends()]
    for f in form.tagged_friends:
        f.username.choices = current_user_friends
    if form.validate_on_submit():
        print(form.data)
        hero_role = int(request.form.get('ow_hero_role'))
        ow_map = request.form.get('ow_map')
        heroes = [int(hero_id) for hero_id in request.form.getlist('ow_heroes')]
        #date_match_played = datetime.strptime(request.form.get('date-match-played'), '%m/%d/%Y') 
        date_match_played = datetime.strptime(request.form.get('datetime-match-played'), '%Y-%m-%d %H:%M') 
        #2022-09-27 13:33
        match_mode = int(request.form.get('match-mode'))
        if match_mode == 1:
            ranked_flag = True
        else: ranked_flag = False
        map_played = Map.query.filter(Map.id==int(ow_map)).first_or_404()
        new_match = Match(created_by_user_id=current_user.id, ranked_flag=ranked_flag, map_played=map_played, date_match_played=date_match_played)
        for hero in heroes:
            a = MatchHero()
            a.hero = Hero.query.filter(Hero.id==int(hero)).first_or_404()
            new_match.heroes_played.append(a)
        for round in form.data['match_rounds']:
            new_match.add_round(phase=round['phase'], score=round['score'])
            #objectives_captured=round['result']
        #new_match.rounds[0].score = 1
        new_match.add_user(user=current_user, accepted_flag=True, hero_role_id=hero_role, heroes_played=heroes)
        for friend in form.data['tagged_friends']:
            if friend['role'] == 'DAMAGE':
                hero_role = 1
            elif friend['role'] == 'SUPPORT':
                hero_role = 2
            elif ['role'] == 'TANK':
                hero_role = 3

            friend = User.query.filter(User.username==friend['username']).first()
            if friend:
                new_match.add_user(user=friend,accepted_flag=False,hero_role_id=hero_role)
        db.session.add(new_match)
        db.session.commit()
        return redirect(url_for('client.dashboard.user_dashboard')) 
    else:
        print(form.errors) 
        return 'not validated'

@match.post('/<int:match_id>')
@login_required
def update_match(match_id):
    print(request.form)
    match_mode = int(request.form.get('match-mode'))
    if match_mode == 1:
        ranked_flag = True
    else: ranked_flag = False
    match = Match.query.filter(Match.id==match_id).first_or_404()
    match.set_ow_map(int(request.form.get('ow_map')))
    match.date_match_played = datetime.strptime(request.form.get('date-match-played'), '%m/%d/%Y')
    match.ranked_flag = ranked_flag
    c_u_match_info = MatchUser.query.filter(and_(MatchUser.match_id==match_id, MatchUser.user_id==current_user.id)).first_or_404()
    c_u_match_info.heroes_played = []
    for hero in [int(hero_id) for hero_id in request.form.getlist('ow_heroes')]:
        c_u_match_info.add_hero(hero_id=int(hero))
    c_u_match_info.hero_role_id = int(request.form.get('ow_hero_role'))
    db.session.commit()
    return redirect(url_for('client.dashboard.user_dashboard')) 


    # form = CreateMatchForm()
    # current_user_friends = [(f, f) for f in user_utils.get_current_user_friends()] + [None]
    # for f in form.tagged_friends:
    #     f.username.choices = current_user_friends
    # if form.validate_on_submit():
    #     print(form.data)
    #     hero_role = int(request.form.get('ow_hero_role'))
    #     ow_map = request.form.get('ow_map')
    #     
    #     date_match_played = datetime.strptime(request.form.get('date-match-played'), '%m/%d/%Y') 
    #     map_played = Map.query.filter(Map.id==int(ow_map)).first_or_404()
    #     new_match = Match(created_by_user_id=current_user.id, ranked_flag=True, map_played=map_played, date_match_played=date_match_played)
    #     for hero in heroes:
    #         a = MatchHero()
    #         a.hero = Hero.query.filter(Hero.id==int(hero)).first_or_404()
    #         new_match.heroes_played.append(a)
    #     for round in form.data['match_rounds']:
    #         new_match.add_round(phase=round['phase'], score=round['score'])
    #         #objectives_captured=round['result']
    #     #new_match.rounds[0].score = 1
    #     new_match.add_user(user=current_user, accepted_flag=True, hero_role_id=hero_role, heroes_played=heroes)
    #     for friend in form.data['tagged_friends']:
    #         if friend['role'] == 'DAMAGE':
    #             hero_role = 1
    #         elif friend['role'] == 'SUPPORT':
    #             hero_role = 2
    #         elif ['role'] == 'TANK':
    #             hero_role = 3

    #         friend = User.query.filter(User.username==friend['username']).first_or_404()
    #         new_match.add_user(user=friend,accepted_flag=False,hero_role_id=hero_role)


    # else:
    #     print(form.errors) 
    #     return 'not validated'

# @match.get('')
# @login_required
# def get_matches():
#     current_user_matches = Match.query.filter(MatchUser.user_id==current_user.id).all()
#     return jsonify(current_user_matches)

@match.post('/<int:match_id>/accept')
@login_required
def accept_match_invite(match_id):
    print(match_id)
    match_user = MatchUser.query.filter(and_(MatchUser.match_id==int(match_id), MatchUser.user_id==current_user.id, MatchUser.accepted_flag==False)).first_or_404()
    match_user.accepted_flag = True
    db.session.commit()
    return redirect(request.referrer)

@match.post('/<int:match_id>/decline')
@login_required
def decline_match_invite(match_id):
    match_user = MatchUser.query.filter(and_(MatchUser.match_id==match_id, MatchUser.user_id==current_user.id, MatchUser.accepted_flag==False)).first_or_404()
    db.session.delete(match_user)
    db.session.commit()
    return redirect(request.referrer)

@match.delete('/<int:match_id>')
@login_required
def delete_match(match_id):
    match = Match.query.join(MatchUser, Match.users)\
                       .filter(and_(Match.id==match_id, MatchUser.user_id==current_user.id, MatchUser.accepted_flag==True))\
                       .first_or_404()
    db.session.delete(match)
    db.session.commit()
    return make_response(jsonify({'MESSAGE': 'MATCH DELETED!'}),200)