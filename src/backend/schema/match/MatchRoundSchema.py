from marshmallow import Schema, fields

class MatchRoundSchema(Schema):
    id = fields.Integer()
    score = fields.Integer()
    phase = fields.String()