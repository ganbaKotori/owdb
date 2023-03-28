from app import db

class Hero(db.Model):
    __tablename__ = "ow_hero"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String(25))
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))
    hero_role = db.relationship("HeroRole")