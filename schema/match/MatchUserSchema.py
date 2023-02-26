from marshmallow import Schema, fields

from routes.api.user.schema import UserSchema

class MatchUserSchema(Schema):
    id = fields.Integer()
    user = fields.Nested(UserSchema)