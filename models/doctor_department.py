from init import db

class DoctorDepartment(db.Model):
    __tablename__ = 'doctor_department'

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), primary_key=True)

    doctor = db.relationship('Doctor', back_populates='departments')
    department = db.relationship('Department', back_populates='doctors')