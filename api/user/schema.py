from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.String()