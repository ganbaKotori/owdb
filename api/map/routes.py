from flask import Blueprint
from api.map.utils import add_all_ow_maps
from api.map.models import Map
from api.match.models import Match, MatchUser, MatchUserHero, MatchResult
from api.hero.models import Hero, HeroRole
from api.user.models import User
from app import db
from flask_login import current_user
from sqlalchemy import func, select
from sqlalchemy import case, cast, Float
map = Blueprint('map', __name__, url_prefix='/map')


@map.post('')
def add_all_maps():
    add_all_ow_maps()
    return 'MAPS ADDED'

@map.get('/<int:map_id>')
def get_map(map_id):
    print(map_id)

    # match_results = db.session.query(func.count(Hero.id), Match.id, Map.name, Hero.name)\
    #                     .group_by(Hero.id)\
    #                     .join(Map, Match.map_played)\
    #                     .join(MatchUser, Match.users)\
    #                     .join(MatchUserHero, MatchUser.heroes_played)\
    #                     .join(Hero, MatchUserHero.hero)\
    #                     .filter(MatchUser.user_id==current_user.id)\
    #                     .filter(Map.id==map_id)\
    #                     .all()
    # for x in match_results:
    #     print(x)

    heroes_played = db.session.query(Hero.id, Match.id, Map.name, Hero.name)\
                        .group_by(Hero.id)\
                        .join(Map, Match.map_played)\
                        .join(MatchUser, Match.users)\
                        .join(MatchUserHero, MatchUser.heroes_played)\
                        .join(Hero, MatchUserHero.hero)\
                        .filter(MatchUser.user_id==current_user.id)\
                        .filter(Map.id==map_id)\
                        .all()
    for x in heroes_played:
        #print(x)
        matches_won = db.session.query(func.count(Match.id), Hero.id, Match.id, Map.name, Hero.name)\
                    .group_by(Hero.id)\
                    .join(Map, Match.map_played)\
                    .join(MatchUser, Match.users)\
                    .join(MatchUserHero, MatchUser.heroes_played)\
                    .join(Hero, MatchUserHero.hero)\
                    .filter(MatchUser.user_id==current_user.id)\
                    .filter(Hero.id==x[0])\
                    .filter(Match.match_result==MatchResult.VICTORY)\
                    .all()
        all_matches = db.session.query(func.count(Match.id), Hero.id, Match.id, Map.name, Hero.name)\
                    .group_by(Hero.id)\
                    .join(Map, Match.map_played)\
                    .join(MatchUser, Match.users)\
                    .join(MatchUserHero, MatchUser.heroes_played)\
                    .join(Hero, MatchUserHero.hero)\
                    .filter(MatchUser.user_id==current_user.id)\
                    .filter(Hero.id==x[0])\
                    .all()
        print(x[3] ,str((matches_won[0][0]/all_matches[0][0]) * 100) + '%')
    return 'MAPS ADDED'
