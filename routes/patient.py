from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Patient
from app.schemas import patient_schema, patients_schema

patient_bp = Blueprint('patient', __name__, url_prefix='/patients')

@patient_bp.route('/', methods=['GET'])
@jwt_required()
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients))

@patient_bp.route('/', methods=['POST'])
@jwt_required()
def add_patient():
    patient = Patient(**request.json)
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient_schema.dump(patient)), 201

@patient_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient_schema.dump(patient))

@patient_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_patient(id):
    patient = Patient.query.get_or_404(id)
    patient.name = request.json['name']
    patient.surname = request.json['surname']
    patient.date_of_birth = request.json['date_of_birth']
    patient.contact_number = request.json['contact_number']
    patient.email = request.json['email']
    db.session.commit()
    return jsonify(patient_schema.dump(patient))

@patient_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204