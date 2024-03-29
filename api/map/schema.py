from marshmallow import Schema, fields

class MapMode(Schema):
    id = fields.Integer()
    max_score = fields.Integer()
    name = fields.String()
    
class MapSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    map_mode = fields.Nested(MapMode)

