from dataclasses import dataclass
from app import db

class MapPre(db.Model):
    __tablename__ = "ow_map"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    map_mode_id = db.Column(db.Integer, db.ForeignKey('ow_map_mode.id'))
    map_mode = db.relationship("MapMode")

    map_stages = db.relationship('MapStage', backref='ow_map')
    
@dataclass
class Map(MapPre):
    id : int
    name : str
    map_mode : MapMode