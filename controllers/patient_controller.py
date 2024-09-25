from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.patient import Patient
from schemas.patient_schema import patient_schema, patients_schema

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

@patients_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients)), 200

@patients_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient_schema.dump(patient)), 200

@patients_bp.route('/', methods=['POST'])
@jwt_required()
def create_patient():
    patient_data = patient_schema.load(request.json)
    patient = Patient(**patient_data)
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient_schema.dump(patient)), 201

@patients_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_patient(id):
    patient = Patient.query.get_or_404(id)
    patient_data = patient_schema.load(request.json, partial=True)
    for key, value in patient_data.items():
        setattr(patient, key, value)
    db.session.commit()
    return jsonify(patient_schema.dump(patient)), 200

@patients_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204