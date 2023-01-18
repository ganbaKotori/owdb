from marshmallow import Schema, fields

from api.user.schema import UserSchema
from api.map.schema import MapSchema

class MatchUserSchema(Schema):
    id = fields.Integer()
    user = fields.Nested(UserSchema)

class MatchRoundSchema(Schema):
    id = fields.Integer()
    score = fields.Integer()
    phase = fields.String()



class MatchSchema(Schema):
    username = fields.String()

    id = fields.Integer()
    ranked_flag : fields.Boolean()
    result_formatted = fields.String()
    date_match_played = fields.DateTime()
    datetime_match_played_formatted = fields.String()
    map_played = fields.Nested(MapSchema)
    
    date_match_played_formatted = fields.String()
    users = fields.List(fields.Nested(MatchUserSchema))
    rounds = fields.List(fields.Nested(MatchRoundSchema))




    