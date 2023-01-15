from marshmallow import Schema, fields

from api.user.schema import UserSchema

class MatchUserSchema(Schema):
    '''    __tablename__ = "ow_match_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    match_id = db.Column(db.Integer, db.ForeignKey('ow_match.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    accepted_flag = db.Column(db.Boolean, nullable=False, default=False)
    #match_owner_flag = db.Column(db.Boolean, nullable=False, default=False)
    hero_role_id = db.Column(db.Integer, db.ForeignKey('ow_hero_role.id'))

    heroes_played = db.relationship("MatchUserHero",cascade="save-update, merge, ""delete, delete-orphan")
    hero_role = db.relationship("HeroRole")
    user = db.relationship("User")'''
    id = fields.Integer()
    user = fields.Nested(UserSchema)


class MatchSchema(Schema):
    username = fields.String()

    id = fields.Integer()
    #map_played : Map
    #heroes_played : List[Hero]
    ranked_flag : fields.Boolean()
    # result : MatchResult
    result_formatted = fields.String()
    date_match_played = fields.DateTime()
    datetime_match_played_formatted = fields.String()
    
    date_match_played_formatted = fields.String()
    users = fields.List(fields.Nested(MatchUserSchema))

    