

import enum
from dataclasses import dataclass
from sqlalchemy import Enum
from app import db

@dataclass
class HeroRole(db.Model):
    id : int
    title : str
    
    __tablename__ = "ow_hero_role"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    title = db.Column(db.String(25), nullable=False, unique=True)

@dataclass
class Hero(db.Model):
    id : int
    name : str
    hero_role_id: int
    hero_role: HeroRole

    __tablename__ = "ow_hero"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))
    hero_role = db.relationship("HeroRole")