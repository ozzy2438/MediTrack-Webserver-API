from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Appointment
from app.schemas import appointment_schema, appointments_schema

appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointments')

@appointment_bp.route('/', methods=['GET'])
@jwt_required()
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify(appointments_schema.dump(appointments))

@appointment_bp.route('/', methods=['POST'])
@jwt_required()
def add_appointment():
    appointment = Appointment(**request.json)
    db.session.add(appointment)
    db.session.commit()
    return jsonify(appointment_schema.dump(appointment)), 201

@appointment_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    return jsonify(appointment_schema.dump(appointment))

@appointment_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    appointment.patient_id = request.json['patient_id']
    appointment.doctor_id = request.json['doctor_id']
    appointment.appointment_time = request.json['appointment_time']
    appointment.status = request.json['status']
    db.session.commit()
    return jsonify(appointment_schema.dump(appointment))

@appointment_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return '', 204