import math
from flask_login import current_user
from routes.api.map.models import Map
from routes.api.hero.models import Hero, HeroRole
from routes.api.match.models import Match, MatchUser, MatchUserHero, Hero
from app import db
from routes.api.user.models import User
from sqlalchemy import and_

def get_current_user_matches(user_id, match_count = None):
    match_query = db.session.query(Match.id, Match.date_match_played)\
            .join(MatchUser, Match.users)\
            .filter(MatchUser.user_id==user_id)\
            .filter(MatchUser.accepted_flag==True)\
            .order_by(Match.date_match_played.desc())\
            .limit(match_count).all()

    for x in match_query:
        print(x[0], x[1])
    if match_count:
        subq = db.session.query(MatchUser.id)\
            .join(
                Match,
                Match.id == MatchUser.match_id
                )\
            .filter(MatchUser.user_id==user_id)\
            .filter(MatchUser.accepted_flag==True)\
            .order_by(Match.id.desc())\
            .limit(match_count).subquery()
    else:
        subq = db.session.query(MatchUser.id)\
            .join(
                Match,
                Match.id == MatchUser.match_id
                )\
            .filter(MatchUser.user_id==user_id)\
            .filter(MatchUser.accepted_flag==True)\
            .order_by(Match.id.desc())\
            .subquery() 

    match_results = db.session.query(Match.id, Map.name, Match.match_result, Match.ranked_flag, Match.date_match_played, User.username, HeroRole.title)\
                        .join(
                        MatchUser,
                        and_(Match.id == MatchUser.match_id, MatchUser.id.in_(subq))
                        )\
                        .join(Map, Match.map_played)\
                        .join(User, Match.created_by_user)\
                        .join(HeroRole, MatchUser.hero_role)\
                        .all()

    match_heroes_results = db.session.query(Match.id, Hero.name)\
                .join(
                        MatchUser,
                        and_(Match.id == MatchUser.match_id, MatchUser.id.in_(subq))
                     )\
                .join(MatchUserHero, MatchUser.heroes_played)\
                .join(Hero, MatchUserHero.hero)\
                .all()
    match_heroes = {}
    for match_id, match_hero in match_heroes_results:
        #print(match_id, match_hero)
        if match_id in match_heroes:
            match_heroes[match_id].append(match_hero)
        else:
            match_heroes[match_id] = [match_hero]
    matches = [] 
    for match_id, map_name, match_result, ranked_flag, date_match_played, submitted_by_username, hero_role in match_results:
        match = {
            "match_id" : match_id,
            "map_name" : map_name,
            "match_result" : match_result.split('.')[1],
            "ranked_flag" : ranked_flag,
            "date_match_played" : date_match_played.strftime("%B %d, %Y @ %I:%M%p"),
            "submitted_by_username" : submitted_by_username,
            "hero_role" : hero_role,
            "heroes_played" : []
        }
        if match_id in match_heroes:
            match['heroes_played'] = match_heroes[match_id]
        matches.append(match)
    return matches