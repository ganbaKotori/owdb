from flask import Blueprint, request, redirect, url_for,  jsonify
from app import db
from api.match.models import Match, MatchPhase, MatchResult, MatchRound, MatchHero, MatchUser
from api.map.models import Map
from api.hero.models import Hero
from api.user.models import User
from flask_login import current_user, login_required
from api.match.forms import CreateMatchForm
import api.user.utils as user_utils
from datetime import datetime

match = Blueprint('match', __name__, url_prefix='/match')

@match.post('')
@login_required
def add_match():
    #print(request.form)
    form = CreateMatchForm()
    current_user_friends = [(f, f) for f in user_utils.get_current_user_friends()]
    for f in form.tagged_friends:
        f.username.choices = current_user_friends
    if form.validate_on_submit():
        print(form.data)
        hero_role = request.form.get('ow_hero_role')
        ow_map = request.form.get('ow_map')
        heroes = [int(hero_id) for hero_id in request.form.getlist('ow_heroes')]
        date_match_played = datetime.strptime(request.form.get('date-match-played'), '%m/%d/%Y') 
        print(date_match_played)
        # print(hero_role)
        # print(ow_map)
        # print(heroes)
        map_played = Map.query.filter(Map.id==int(ow_map)).first_or_404()
        new_match = Match(created_by_user_id=current_user.id, ranked_flag=True, map_played=map_played, date_match_played=date_match_played)
        for hero in heroes:
            a = MatchHero()
            a.hero = Hero.query.filter(Hero.id==int(hero)).first_or_404()
            new_match.heroes_played.append(a)
        for round in form.data['match_rounds']:
            new_match.add_round(phase=round['phase'], score=round['score'])
            #objectives_captured=round['result']
        #new_match.rounds[0].score = 1
        new_match.add_user(user=current_user, accepted_flag=True, heroes_played=heroes)
        for friend in form.data['tagged_friends']:
            friend = User.query.filter(User.username==friend['username']).first_or_404()
            new_match.add_user(user=friend, accepted_flag=False)
        db.session.add(new_match)
        db.session.commit()
        return redirect(url_for('client.dashboard.user_dashboard')) 
    else:
        print(form.errors) 
        return 'not validated'

@match.get('')
@login_required
def get_matches():
    current_user_matches = Match.query.filter(MatchUser.user_id==current_user.id).all()
    return jsonify(current_user_matches)