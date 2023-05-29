
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