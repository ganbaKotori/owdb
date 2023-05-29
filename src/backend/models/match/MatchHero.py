from app import db

class MatchHero(db.Model):
    __tablename__ = 'ow_match_hero'
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    hero = db.relationship("Hero")