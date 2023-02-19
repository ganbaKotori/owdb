
from models.map.Map import Map

from models.match.Match import Match
from models.match.MatchUser import MatchUser
from models.match.MatchUserHero import MatchUserHero
from models.match.MatchResult import MatchResult
from models.hero.Hero import Hero
from models.hero.HeroRole import HeroRole
from models.user.User import User
from app import db
from sqlalchemy import func

def get_heroes_winrate(user: User, map_id: int, hero_role_id: int):
    hero_stats = []
    heroes_played = db.session.query(Hero.id, Match.id, Map.name, Hero.name)\
                        .group_by(Hero.id)\
                        .join(Map, Match.map_played)\
                        .join(MatchUser, Match.users)\
                        .join(MatchUserHero, MatchUser.heroes_played)\
                        .join(Hero, MatchUserHero.hero)\
                        .join(HeroRole, Hero.hero_role)\
                        .filter(MatchUser.user_id==user.id)\
                        .filter(Map.id==map_id)\
                        .filter(HeroRole.id==hero_role_id)\
                        .all()
    for x in heroes_played:
        matches_won = db.session.query(func.count(Match.id), Hero.id, Match.id, Map.name, Hero.name)\
                    .group_by(Hero.id)\
                    .join(Map, Match.map_played)\
                    .join(MatchUser, Match.users)\
                    .join(MatchUserHero, MatchUser.heroes_played)\
                    .join(Hero, MatchUserHero.hero)\
                    .filter(MatchUser.user_id==user.id)\
                    .filter(Hero.id==x[0])\
                    .filter(Match.match_result==MatchResult.VICTORY)\
                    .all()
        all_matches = db.session.query(func.count(Match.id), Hero.id, Match.id, Map.name, Hero.name)\
                    .group_by(Hero.id)\
                    .join(Map, Match.map_played)\
                    .join(MatchUser, Match.users)\
                    .join(MatchUserHero, MatchUser.heroes_played)\
                    .join(Hero, MatchUserHero.hero)\
                    .filter(MatchUser.user_id==user.id)\
                    .filter(Hero.id==x[0])\
                    .all()
        if len(matches_won) == 0:
            hero_stats.append({
            'hero_name' : x[3],
            'win_rate' : 0
        })
        else:
            print(x[3] ,str((matches_won[0][0]/all_matches[0][0]) * 100) + '%')
            hero_stats.append({
                'hero_name' : x[3],
                'win_rate' : (matches_won[0][0]/all_matches[0][0]) * 100
            })

    return sorted(hero_stats, key=lambda d: d['win_rate'], reverse=True) 