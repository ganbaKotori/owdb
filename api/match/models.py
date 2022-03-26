import enum
from dataclasses import dataclass
from sqlalchemy import Enum
from app import db
from api.hero.models import Hero


class MatchResult(enum.Enum):
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"
    DRAW = "DRAW"

class MatchPhase(enum.Enum):
    ATTACK = "VICTORY"
    DEFEND = "DEFEAT"
    CONTROL = "CONTROL"

class MatchRoundResult(enum.Enum):
    SUCESS = "SUCESS"
    FAIL = "FAIL"


@dataclass
class Match(db.Model):
    __tablename__ = "ow_match"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    map_played_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ranked_flag = db.Column(db.Boolean)
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))

    map_played = db.relationship("Map")
    rounds = db.relationship('MatchRound', backref='match')
    hero_role = db.relationship('HeroRole', backref='hero_role')
    
    heroes_played = db.relationship("MatchHero")

    result = db.Column(Enum(MatchResult))

@dataclass
class MatchRound(db.Model):
    __tablename__ = "ow_match_round"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))

@dataclass
class MatchHero(db.Model):
    __tablename__ = 'ow_match_hero'
    hero_id = db.Column(db.ForeignKey('ow_hero.id'), primary_key=True)
    match_id = db.Column(db.ForeignKey('ow_match.id'), primary_key=True)
    hero = db.relationship("Hero")