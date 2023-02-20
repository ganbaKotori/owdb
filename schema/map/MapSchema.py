from marshmallow import Schema, fields
from schema.map.MapModeSchema import MapModeSchema

class MapSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    map_mode = fields.Nested(MapModeSchema)