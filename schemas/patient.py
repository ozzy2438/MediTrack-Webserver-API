from app import ma
from app.models import Patient

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)