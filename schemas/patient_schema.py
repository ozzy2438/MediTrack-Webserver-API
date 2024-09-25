from marshmallow import Schema, fields, validate

class PatientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    surname = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    date_of_birth = fields.Date(required=True)
    contact_number = fields.Str(validate=validate.Length(max=20))
    email = fields.Email()

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)