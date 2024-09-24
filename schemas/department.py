from app import ma
from app.models import Department, DoctorDepartment

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department

class DoctorDepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DoctorDepartment

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
doctor_department_schema = DoctorDepartmentSchema()
doctor_departments_schema = DoctorDepartmentSchema(many=True)