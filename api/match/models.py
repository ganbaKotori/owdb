import enum
from api.user.models import User
from dataclasses import dataclass
from sqlalchemy import Enum
from app import db
from api.hero.models import Hero
from api.map.models import Map


from typing import List
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
from datetime import datetime

class MatchResult(enum.Enum):
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"
    DRAW = "DRAW"

class MatchPhase(enum.Enum):
    ATTACK = "ATTACK"
    DEFEND = "DEFEND"

@dataclass
class Match(db.Model):
    id: int
    map_played : Map
    heroes_played : List[Hero]
    ranked_flag : bool
    result : MatchResult
    result_formatted : str

    roles : List[str]

    __tablename__ = "ow_match"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    map_played_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_played = db.Column(db.DateTime(), default=datetime.utcnow())
    ranked_flag = db.Column(db.Boolean, nullable=False, default=True)

    map_played = db.relationship("Map")
    rounds = db.relationship('MatchRound', backref='match')
    
    heroes_played = db.relationship("MatchHero")
    tagged_users = db.relationship("MatchTaggedUser")

    result = db.Column(Enum(MatchResult))

    @property
    def roles(self):
        match_roles = []
        if self.tank_hero_count > 0:
            match_roles.append("Tank")
        if self.damage_hero_count > 0:
            match_roles.append("Damage")
        if self.support_hero_count > 0:
            match_roles.append("Support")
        return match_roles

    @property
    def result_formatted(self):
        return self.result.value

    @hybrid_property
    def tank_hero_count(self):
        return sum([1 for p in self.heroes_played if p.hero.hero_role.title == "Tank"])   # @note: use when non-dynamic relationship

    @tank_hero_count.expression
    def tank_hero_count(cls):
        return (select([func.count(MatchHero.hero_id)]).
                where(MatchHero.match_id == cls.id).
                label("tank_hero_count")
                )

    @hybrid_property
    def damage_hero_count(self):
        return sum([1 for p in self.heroes_played if p.hero.hero_role.title == "Damage"])   # @note: use when non-dynamic relationship

    @damage_hero_count.expression
    def damage_hero_count(cls):
        return (select([func.count(MatchHero.hero_id)]).
                where(MatchHero.match_id == cls.id).
                label("damage_hero_count")
                )

    @hybrid_property
    def support_hero_count(self):
        return sum([1 for p in self.heroes_played if p.hero.hero_role.title == "Support"])   # @note: use when non-dynamic relationship

    @support_hero_count.expression
    def support_hero_count(cls):
        return (select([func.count(MatchHero.hero_id)]).
                where(MatchHero.match_id == cls.id).
                label("support_hero_count")
                )

    def add_tagged_user(self):
        self.tagged_users.append()
        self.requested_friends.append(MatchTaggedUser(user_id=self.id))

    def add_round(self, objectives_captured, phase):
        if phase == "ATTACK":
            phase_value = MatchPhase.ATTACK
        elif phase == "DEFEND":
            phase_value = MatchPhase.DEFEND
        if objectives_captured == "1":
            objs_captured_value = True
        elif objectives_captured == "0":
            objs_captured_value = False
        new_round = MatchRound(objectives_captured=objs_captured_value, phase=phase_value)
        self.rounds.append(new_round)


@dataclass
class MatchRound(db.Model):
    __tablename__ = "ow_match_round"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    objectives_captured = db.Column(db.Boolean, nullable=False, default=False)
    phase = db.Column(Enum(MatchPhase))

@dataclass
class MatchHero(db.Model):
    hero : Hero

    __tablename__ = 'ow_match_hero'
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    hero = db.relationship("Hero")

@dataclass
class MatchTaggedUser(db.Model):

    __tablename__ = "ow_match_tagged_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
