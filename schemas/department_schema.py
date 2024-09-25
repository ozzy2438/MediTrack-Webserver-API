from marshmallow import Schema, fields, validate

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str()

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)