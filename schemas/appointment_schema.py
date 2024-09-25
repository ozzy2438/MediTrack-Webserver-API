from marshmallow import Schema, fields, validate

class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    patient_id = fields.Int(required=True)
    doctor_id = fields.Int(required=True)
    appointment_time = fields.DateTime(required=True)
    status = fields.Str(required=True, validate=validate.OneOf(["Scheduled", "Completed", "Cancelled"]))

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)