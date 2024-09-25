from marshmallow import Schema, fields, validate

class DoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    surname = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    specialization = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    contact_number = fields.Str(validate=validate.Length(max=20))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)