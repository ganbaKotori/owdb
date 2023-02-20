from marshmallow import Schema, fields

class MapModeSchema(Schema):
    id = fields.Integer()
    max_score = fields.Integer()
    name = fields.String()
    