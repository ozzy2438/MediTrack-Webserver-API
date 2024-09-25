from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.doctor import Doctor
from models.department import Department
from schemas.doctor_schema import doctor_schema
from schemas.department_schema import department_schema

doctor_department_bp = Blueprint('doctor_department', __name__, url_prefix='/doctor_department')

@doctor_department_bp.route('/', methods=['POST'])
@jwt_required()
def assign_doctor_to_department():
    data = request.json
    doctor_id = data.get('doctor_id')
    department_id = data.get('department_id')

    doctor = Doctor.query.get_or_404(doctor_id)
    department = Department.query.get_or_404(department_id)

    if department not in doctor.departments:
        doctor.departments.append(department)
        db.session.commit()
        return jsonify({
            'message': 'Doctor assigned to department successfully',
            'doctor': doctor_schema.dump(doctor),
            'department': department_schema.dump(department)
        }), 201
    else:
        return jsonify({'message': 'Doctor is already assigned to this department'}), 400

@doctor_department_bp.route('/', methods=['DELETE'])
@jwt_required()
def remove_doctor_from_department():
    data = request.json
    doctor_id = data.get('doctor_id')
    department_id = data.get('department_id')

    doctor = Doctor.query.get_or_404(doctor_id)
    department = Department.query.get_or_404(department_id)

    if department in doctor.departments:
        doctor.departments.remove(department)
        db.session.commit()
        return jsonify({'message': 'Doctor removed from department successfully'}), 200
    else:
        return jsonify({'message': 'Doctor is not assigned to this department'}), 400

@doctor_department_bp.route('/doctor/<int:doctor_id>', methods=['GET'])
@jwt_required()
def get_doctor_departments(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return jsonify({
        'doctor': doctor_schema.dump(doctor),
        'departments': department_schema.dump(doctor.departments, many=True)
    }), 200

@doctor_department_bp.route('/department/<int:department_id>', methods=['GET'])
@jwt_required()
def get_department_doctors(department_id):
    department = Department.query.get_or_404(department_id)
    return jsonify({
        'department': department_schema.dump(department),
        'doctors': doctor_schema.dump(department.doctors, many=True)
    }), 200