from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from init import db, bcrypt
from models.doctor import Doctor
from schemas.doctor_schema import doctor_schema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        doctor_data = doctor_schema.load(request.json)
        doctor = Doctor(
            name=doctor_data['name'],
            email=doctor_data['email'],
            password=bcrypt.generate_password_hash(doctor_data['password']).decode('utf-8')
        )
        db.session.add(doctor)
        db.session.commit()
        return jsonify(doctor_schema.dump(doctor)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    doctor_data = request.json
    doctor = Doctor.query.filter_by(email=doctor_data.get('email')).first()

    if doctor and bcrypt.check_password_hash(doctor.password, doctor_data.get('password')):
        token = create_access_token(identity=str(doctor.id), expires_delta=timedelta(days=1))
        return jsonify({'doctor': doctor_schema.dump(doctor), 'token': token}), 200
    
    return jsonify({'error': 'Invalid email or password'}), 401