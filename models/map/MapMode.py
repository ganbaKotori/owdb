from dataclasses import dataclass
from app import db


@dataclass
class MapMode(db.Model):
    id : int
    max_score : int
    name : str
    
    __tablename__ = "ow_map_mode"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    max_score =  db.Column(db.Integer)
    name = db.Column(db.String(25))
