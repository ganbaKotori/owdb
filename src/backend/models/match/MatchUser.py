from app import db

class MatchUser(db.Model):
    __tablename__ = "ow_match_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    accepted_flag = db.Column(db.Boolean, nullable=False, default=False)
    #match_owner_flag = db.Column(db.Boolean, nullable=False, default=False)
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))

    heroes_played = db.relationship("MatchUserHero",cascade="save-update, merge, ""delete, delete-orphan")
    hero_role = db.relationship("HeroRole")
    user = db.relationship("User")

    def add_hero(self, hero_id):
        match_user_hero = MatchUserHero()
        match_user_hero.hero = Hero.query.filter(Hero.id==int(hero_id)).first_or_404()
        self.heroes_played.append(match_user_hero)
