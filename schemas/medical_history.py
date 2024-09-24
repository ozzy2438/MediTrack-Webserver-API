from app import ma
from app.models import PatientMedicalHistory

class PatientMedicalHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PatientMedicalHistory

medical_history_schema = PatientMedicalHistorySchema()
medical_histories_schema = PatientMedicalHistorySchema(many=True)