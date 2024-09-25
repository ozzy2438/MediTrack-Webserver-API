from marshmallow import Schema, fields
from models.department import Department

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)