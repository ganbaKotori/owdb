from flask import Blueprint
from app import db
from api.match.models import Match, MatchPhase, MatchResult, MatchRound, MatchHero
from api.map.models import Map
from api.hero.models import Hero
from flask_login import current_user

match = Blueprint('match', __name__, url_prefix='/match')


@match.post('')
def add_match():
    map_played = Map.query.filter(Map.id==1).first_or_404()
    initial_map_round = MatchRound()
    new_match = Match(user_id=current_user.id, ranked_flag=True, map_played=map_played, rounds=[initial_map_round], result=MatchResult.VICTORY)
    a = MatchHero()
    a.hero = Hero.query.filter(Hero.id==1).first_or_404()
    new_match.heroes_played.append(a)
    print(new_match)
    db.session.add(new_match)
    db.session.commit()
    return "MATCH ADDED"