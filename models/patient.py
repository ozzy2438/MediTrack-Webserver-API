from init import db

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  # Yeni eklenen alan
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)

    appointments = db.relationship('Appointment', back_populates='patient', cascade='all, delete-orphan')
    medical_history = db.relationship('PatientMedicalHistory', back_populates='patient', cascade='all, delete-orphan')