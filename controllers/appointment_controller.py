from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.appointment import Appointment
from schemas.appointment_schema import appointment_schema, appointments_schema

appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@appointments_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_appointments():
    appointments = Appointment.query.all()
    return jsonify(appointments_schema.dump(appointments)), 200

@appointments_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    return jsonify(appointment_schema.dump(appointment)), 200

@appointments_bp.route('/', methods=['POST'])
@jwt_required()
def create_appointment():
    appointment_data = appointment_schema.load(request.json)
    appointment = Appointment(**appointment_data)
    db.session.add(appointment)
    db.session.commit()
    return jsonify(appointment_schema.dump(appointment)), 201

@appointments_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    appointment_data = appointment_schema.load(request.json, partial=True)
    for key, value in appointment_data.items():
        setattr(appointment, key, value)
    db.session.commit()
    return jsonify(appointment_schema.dump(appointment)), 200

@appointments_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return '', 204