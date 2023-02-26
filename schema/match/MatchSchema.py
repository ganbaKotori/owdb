from marshmallow import Schema, fields

from schema.map.MapSchema import MapSchema
from schema.match.MatchUserSchema import MatchUserSchema
from schema.match.MatchRoundSchema import MatchRoundSchema

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