from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.doctor import Doctor
from schemas.doctor_schema import doctor_schema, doctors_schema

doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@doctors_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_doctors():
    doctors = Doctor.query.all()
    return jsonify(doctors_schema.dump(doctors)), 200

@doctors_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    return jsonify(doctor_schema.dump(doctor)), 200

@doctors_bp.route('/', methods=['POST'])
@jwt_required()
def create_doctor():
    doctor_data = doctor_schema.load(request.json)
    new_doctor = Doctor(
        name=doctor_data['name'],
        surname=doctor_data['surname'],
        specialization=doctor_data['specialization'],
        contact_number=doctor_data.get('contact_number'),
        email=doctor_data['email'],
        password=doctor_data['password']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(doctor_schema.dump(new_doctor)), 201

@doctors_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    doctor_data = doctor_schema.load(request.json, partial=True)
    for key, value in doctor_data.items():
        setattr(doctor, key, value)
    db.session.commit()
    return jsonify(doctor_schema.dump(doctor)), 200

@doctors_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    db.session.delete(doctor)
    db.session.commit()
    return '', 204