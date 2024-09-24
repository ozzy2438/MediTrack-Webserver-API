from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Department, DoctorDepartment
from app.schemas import department_schema, departments_schema, doctor_department_schema

department_bp = Blueprint('department', __name__, url_prefix='/departments')

@department_bp.route('/', methods=['GET'])
@jwt_required()
def get_departments():
    departments = Department.query.all()
    return jsonify(departments_schema.dump(departments))

@department_bp.route('/', methods=['POST'])
@jwt_required()
def add_department():
    department = Department(**request.json)
    db.session.add(department)
    db.session.commit()
    return jsonify(department_schema.dump(department)), 201

@department_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_department(id):
    department = Department.query.get_or_404(id)
    return jsonify(department_schema.dump(department))

@department_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_department(id):
    department = Department.query.get_or_404(id)
    department.name = request.json['name']
    department.description = request.json['description']
    db.session.commit()
    return jsonify(department_schema.dump(department))

@department_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return '', 204

@department_bp.route('/<int:id>/doctors', methods=['POST'])
@jwt_required()
def add_doctor_to_department(id):
    doctor_department = DoctorDepartment(doctor_id=request.json['doctor_id'], department_id=id)
    db.session.add(doctor_department)
    db.session.commit()
    return jsonify(doctor_department_schema.dump(doctor_department)), 201