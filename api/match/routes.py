from flask import Blueprint, request, redirect, url_for,  jsonify
from app import db
from api.match.models import Match, MatchPhase, MatchResult, MatchRound, MatchHero
from api.map.models import Map
from api.hero.models import Hero
from flask_login import current_user, login_required
from api.match.forms import CreateMatchForm

match = Blueprint('match', __name__, url_prefix='/match')


@match.post('')
@login_required
def add_match():
    #print(request.form)
    form = CreateMatchForm()
    if form.validate_on_submit():
        print(form.data)
        hero_role = request.form.get('ow_hero_role')
        ow_map = request.form.get('ow_map')
        heroes = request.form.getlist('ow_heroes')
        print(hero_role)
        print(ow_map)
        print(heroes)
        map_played = Map.query.filter(Map.id==int(ow_map)).first_or_404()
        initial_map_round = MatchRound()
        new_match = Match(user_id=current_user.id, ranked_flag=True, map_played=map_played, rounds=[initial_map_round], result=MatchResult.VICTORY)
        for hero in heroes:
            a = MatchHero()
            a.hero = Hero.query.filter(Hero.id==int(hero)).first_or_404()
            new_match.heroes_played.append(a)
        print(new_match)
        db.session.add(new_match)
        db.session.commit()
        return redirect(url_for('client.dashboard.user_dashboard')) 
    else:
        print(form.errors) 
        return 'not validated'

@match.get('')
@login_required
def get_matches():
    current_user_matches = Match.query.filter(Match.user_id==current_user.id).all()
    return jsonify(current_user_matches)