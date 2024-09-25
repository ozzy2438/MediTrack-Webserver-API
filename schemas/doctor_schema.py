from marshmallow import Schema, fields, post_load
from models.doctor import Doctor

class DoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    specialization = fields.Str(required=True)
    contact_number = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

    @post_load
    def make_doctor(self, data, **kwargs):
        return data  # Burayı değiştirdik

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)