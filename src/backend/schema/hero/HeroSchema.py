from marshmallow import Schema, fields
from schema.hero.HeroRoleSchema import HeroRoleSchema

class HeroSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    hero_role = fields.Nested(HeroRoleSchema)