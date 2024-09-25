from init import db
from .associations import doctor_department

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    doctors = db.relationship('Doctor', secondary=doctor_department, back_populates='departments')