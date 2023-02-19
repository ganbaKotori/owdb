from app import db

class MatchUserHero(db.Model):
    __tablename__ = 'ow_match_user_hero'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'), primary_key=True)
    match_user_id = db.Column(db.Integer, db.ForeignKey('ow_match_user.id'), primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('ow_hero.id'), primary_key=True)

    hero = db.relationship("Hero")