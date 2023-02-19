import enum
from sqlalchemy import Enum
from app import db
from models.match.MatchPhase import MatchPhase

class MatchRound(db.Model):
    __tablename__ = "ow_match_round"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    phase = db.Column(Enum(MatchPhase))

    score = db.Column(db.Integer, nullable=False, default=0)