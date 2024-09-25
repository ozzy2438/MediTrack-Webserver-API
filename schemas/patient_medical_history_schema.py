from marshmallow import Schema, fields
from models.patient_medical_history import PatientMedicalHistory

class PatientMedicalHistorySchema(Schema):
    id = fields.Int(dump_only=True)
    patient_id = fields.Int(required=True)
    record_date = fields.Date(required=True)
    diagnosis = fields.Str(required=True)
    treatment = fields.Str(required=True)

patient_medical_history_schema = PatientMedicalHistorySchema()
patient_medical_histories_schema = PatientMedicalHistorySchema(many=True)