from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.department import Department
from schemas.department_schema import department_schema, departments_schema

departments_bp = Blueprint('departments', __name__, url_prefix='/departments')

@departments_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_departments():
    departments = Department.query.all()
    return jsonify(departments_schema.dump(departments)), 200

@departments_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_department(id):
    department = Department.query.get_or_404(id)
    return jsonify(department_schema.dump(department)), 200

@departments_bp.route('/', methods=['POST'])
@jwt_required()
def create_department():
    department_data = department_schema.load(request.json)
    department = Department(**department_data)
    db.session.add(department)
    db.session.commit()
    return jsonify(department_schema.dump(department)), 201

@departments_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_department(id):
    department = Department.query.get_or_404(id)
    department_data = department_schema.load(request.json, partial=True)
    for key, value in department_data.items():
        setattr(department, key, value)
    db.session.commit()
    return jsonify(department_schema.dump(department)), 200

@departments_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return '', 204