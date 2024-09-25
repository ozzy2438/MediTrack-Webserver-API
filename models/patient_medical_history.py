from init import db

class PatientMedicalHistory(db.Model):
    __tablename__ = 'patient_medical_history'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    record_date = db.Column(db.Date, nullable=False)
    diagnosis = db.Column(db.String(200), nullable=False)
    treatment = db.Column(db.Text, nullable=False)

    patient = db.relationship('Patient', back_populates='medical_history')