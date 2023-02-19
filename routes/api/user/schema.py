from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()


class UserSchema(Schema):
    username = fields.String()
    
class FriendshipSchema(Schema):
    id = fields.Integer()
    user = fields.Nested(UserSchema)