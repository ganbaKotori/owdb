import enum
from dataclasses import dataclass
from sqlalchemy import Enum
from app import db
from api.hero.models import Hero
from api.map.models import Map
from sqlalchemy.sql.functions import coalesce


from typing import List
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
from datetime import datetime
from sqlalchemy.sql import case
from flask_login import current_user

class MatchResult(enum.Enum):
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"
    DRAW = "DRAW"

class MatchPhase(enum.Enum):
    ATTACK = "ATTACK"
    DEFEND = "DEFEND"

    def __str__(self):
        return self.value

@dataclass
class MatchUserHero(db.Model):
    hero : Hero

    __tablename__ = 'ow_match_user_hero'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    match_user_id = db.Column(db.Integer, db.ForeignKey('ow_match_user.id'), primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)

    hero = db.relationship("Hero")

@dataclass
class MatchUser(db.Model):

    __tablename__ = "ow_match_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    accepted_flag = db.Column(db.Boolean, nullable=False, default=False)
    #match_owner_flag = db.Column(db.Boolean, nullable=False, default=False)
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))

    heroes_played = db.relationship("MatchUserHero",cascade="save-update, merge, ""delete, delete-orphan")
    hero_role = db.relationship("HeroRole")
    user = db.relationship("User")

    def add_hero(self, hero_id):
        match_user_hero = MatchUserHero()
        match_user_hero.hero = Hero.query.filter(Hero.id==int(hero_id)).first_or_404()
        self.heroes_played.append(match_user_hero)

@dataclass
class Match(db.Model):
    id: int
    map_played : Map
    heroes_played : List[Hero]
    ranked_flag : bool
    # result : MatchResult
    result_formatted : str
    date_match_played : datetime
    datetime_match_played_formatted : str
    date_match_played_formatted : str

    roles : List[str]

    users : MatchUser

    current_user_heroes: List[MatchUserHero]

    team_score_formatted : int
    enemy_score_formatted : int

    __tablename__ = "ow_match"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    map_played_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_match_played = db.Column(db.DateTime(), default=datetime.utcnow())
    date_match_created = db.Column(db.DateTime(), default=datetime.utcnow())
    ranked_flag = db.Column(db.Boolean, nullable=False, default=True)

    map_played = db.relationship("Map")
    rounds = db.relationship('MatchRound', backref='match', cascade="save-update, merge, ""delete, delete-orphan")
    
    heroes_played = db.relationship("MatchHero", cascade="save-update, merge, ""delete, delete-orphan")
    users = db.relationship("MatchUser", cascade="save-update, merge, ""delete, delete-orphan")
    created_by_user = db.relationship("User")

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

    # @property
    # def result_formatted(self):
    #     return self.result.value
    @property
    def ranked_flag_formatted(self):
        return "Yes" if self.ranked_flag is True else "No"

    @property
    def result_formatted(self):
        return self.match_result.value

    @property
    def datetime_match_played_formatted(self):
        return self.date_match_played.strftime("%B %d, %Y @ %H:%M%p")
        
    @property
    def date_match_played_formatted(self):
        return self.date_match_played.strftime("%B/%d/%Y")

    @property
    def current_user_heroes(self):
        return next((x.heroes_played for x in self.users if x.user_id == current_user.id), None)

    @hybrid_property
    def tank_hero_count(self):
        return sum([1 for p in self.heroes_played if p.hero.hero_role.title == "Tank"])

    @tank_hero_count.expression
    def tank_hero_count(cls):
        return (select([func.count(MatchHero.hero_id)]).
                where(MatchHero.match_id == cls.id).
                label("tank_hero_count")
                )

    @hybrid_property
    def damage_hero_count(self):
        return sum([1 for p in self.heroes_played if p.hero.hero_role.title == "Damage"])

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
        return (select([func.sum(MatchHero.hero_id)]).
                where(MatchHero.match_id == cls.id).
                label("support_hero_count")
                )

    def add_user(self, user, accepted_flag, hero_role_id, heroes_played = []):
        match_user = MatchUser(match_id = self.id, user_id = user.id, accepted_flag = accepted_flag, hero_role_id = hero_role_id)
        for hero_id in heroes_played:
            match_user.add_hero(hero_id=hero_id)
        self.users.append(match_user)

    def add_round(self, score, phase):
        if phase == "ATTACK":
            phase_value = MatchPhase.ATTACK
        elif phase == "DEFEND":
            phase_value = MatchPhase.DEFEND
        new_round = MatchRound(score=score, phase=phase_value)
        self.rounds.append(new_round)

    # @hybrid_property
    # def result(self):
    #     user_team_score = 0
    #     enemy_team_score = 0
    #     for round in self.rounds:
    #         if round.phase == MatchPhase.ATTACK:
    #             user_team_score += round.score
    #         elif round.phase == MatchPhase.DEFEND:
    #             enemy_team_score += round.score
        

    # @result.expression
    # def result(cls):
    #     return (select([func.count(MatchHero.hero_id)]).
    #             where(MatchHero.match_id == cls.id).
    #             label("support_hero_count")
    #             )   

    @hybrid_property
    def team_score(self):
        user_team_score = 0
        for round in self.rounds:
            if round.phase == MatchPhase.ATTACK:
                user_team_score += round.score
        return user_team_score
        
    #team score and enemy score
    
    @team_score.expression
    def team_score(cls):
        return (select([func.sum(MatchRound.score)]).
                where(MatchRound.phase == MatchPhase.ATTACK).
                where(MatchRound.match_id == cls.id).
                label("match_round_team_score")
                )   

    @property
    def team_score_formatted(self):
        return self.team_score
    
    @hybrid_property
    def enemy_team_score(self):
        enemy_team_score = 0
        for round in self.rounds:
            if round.phase == MatchPhase.DEFEND:
                enemy_team_score += round.score
        return enemy_team_score
        
    #team score and enemy score
    
    @enemy_team_score.expression
    def enemy_team_score(cls):
        return (select([func.sum(MatchRound.score)]).
                where(MatchRound.phase == MatchPhase.DEFEND).
                where(MatchRound.match_id == cls.id).
                label("match_round_enemy_score")
                )

    @property
    def enemy_score_formatted(self):
        return self.enemy_team_score

    @hybrid_property
    def match_result(self):
        if self.team_score > self.enemy_team_score:
            return MatchResult.VICTORY
        elif self.team_score < self.enemy_team_score:
            return MatchResult.DEFEAT
        else: return MatchResult.DRAW
        
    #team score and enemy score
    
    @match_result.expression
    def match_result(cls):
        return case([
            (coalesce(cls.team_score, 0) > coalesce(cls.enemy_team_score, 0) , MatchResult.VICTORY),
            (coalesce(cls.team_score, 0)  < coalesce(cls.enemy_team_score, 0) , MatchResult.DEFEAT),
        ], else_ = MatchResult.DRAW)

    def set_ow_map(self, map_id):
        self.map_played = Map.query.filter(Map.id==map_id).first_or_404()


@dataclass
class MatchRound(db.Model):
    __tablename__ = "ow_match_round"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    phase = db.Column(Enum(MatchPhase))

    score = db.Column(db.Integer, nullable=False, default=0)

@dataclass
class MatchHero(db.Model):
    hero : Hero

    __tablename__ = 'ow_match_hero'
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    hero = db.relationship("Hero")