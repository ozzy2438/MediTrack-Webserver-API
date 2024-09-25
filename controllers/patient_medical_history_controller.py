from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.patient_medical_history import PatientMedicalHistory
from schemas.patient_medical_history_schema import patient_medical_history_schema, patient_medical_histories_schema

patient_medical_history_bp = Blueprint('patient_medical_history', __name__, url_prefix='/patient_medical_history')

@patient_medical_history_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_patient_medical_histories():
    histories = PatientMedicalHistory.query.all()
    return jsonify(patient_medical_histories_schema.dump(histories)), 200

@patient_medical_history_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_patient_medical_history(id):
    history = PatientMedicalHistory.query.get_or_404(id)
    return jsonify(patient_medical_history_schema.dump(history)), 200

@patient_medical_history_bp.route('/', methods=['POST'])
@jwt_required()
def create_patient_medical_history():
    history_data = patient_medical_history_schema.load(request.json)
    history = PatientMedicalHistory(**history_data)
    db.session.add(history)
    db.session.commit()
    return jsonify(patient_medical_history_schema.dump(history)), 201

@patient_medical_history_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_patient_medical_history(id):
    history = PatientMedicalHistory.query.get_or_404(id)
    history_data = patient_medical_history_schema.load(request.json, partial=True)
    for key, value in history_data.items():
        setattr(history, key, value)
    db.session.commit()
    return jsonify(patient_medical_history_schema.dump(history)), 200

@patient_medical_history_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient_medical_history(id):
    history = PatientMedicalHistory.query.get_or_404(id)
    db.session.delete(history)
    db.session.commit()
    return '', 204