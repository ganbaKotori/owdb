from dataclasses import dataclass
from sqlalchemy import Enum
from app import db

@dataclass
class MatchUserHero(db.Model):
    hero : Hero

    __tablename__ = 'ow_match_user_hero'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    match_user_id = db.Column(db.Integer, db.ForeignKey('ow_match_user.id'), primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)

    hero = db.relationship("Hero")