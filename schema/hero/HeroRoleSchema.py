
from marshmallow import Schema, fields

class HeroRoleSchema(Schema):
    id = fields.Integer()
    title = fields.String()