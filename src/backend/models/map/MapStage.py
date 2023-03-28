from dataclasses import dataclass
from app import db


@dataclass
class MapStage(db.Model):
    __tablename__ = "ow_match_stage"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    ow_map_id = db.Column(db.Integer, db.ForeignKey('ow_map.id'))

