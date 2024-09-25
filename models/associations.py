from init import db

doctor_department = db.Table('doctor_department',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id'), primary_key=True),
    db.Column('department_id', db.Integer, db.ForeignKey('departments.id'), primary_key=True)
)