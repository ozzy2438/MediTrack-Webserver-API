from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(100))
    appointments = db.relationship('Appointment', backref='patient', lazy='dynamic')
    medical_history = db.relationship('PatientMedicalHistory', backref='patient', lazy='dynamic')