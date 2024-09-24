from app import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    doctors = db.relationship('DoctorDepartment', back_populates='department')

class DoctorDepartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    doctor = db.relationship('Doctor', back_populates='departments')
    department = db.relationship('Department', back_populates='doctors')