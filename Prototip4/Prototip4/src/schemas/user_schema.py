from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=6))
    idrole = fields.Int(required=True)