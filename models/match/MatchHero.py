from dataclasses import dataclass
from sqlalchemy import Enum
from app import db

@dataclass
class MatchHero(db.Model):
    hero : Hero

    __tablename__ = 'ow_match_hero'
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    hero = db.relationship("Hero")