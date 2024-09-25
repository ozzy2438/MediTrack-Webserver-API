from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from init import db, bcrypt
from models.doctor import Doctor
from schemas.doctor_schema import doctor_schema
from marshmallow import ValidationError

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    doctor_data = request.json
    try:
        # Şemayı kullanarak doğrulama ve dönüştürme işlemi
        validated_data = doctor_schema.load(doctor_data)
        
        # Şifreyi hash'leme
        hashed_password = bcrypt.generate_password_hash(validated_data['password']).decode('utf-8')
        
        # Yeni doktor nesnesini oluşturma
        new_doctor = Doctor(
            name=validated_data['name'],
            surname=validated_data['surname'],
            specialization=validated_data['specialization'],
            contact_number=validated_data.get('contact_number'),
            email=validated_data['email'],
            password=hashed_password
        )
        
        # Veritabanına kaydetme
        db.session.add(new_doctor)
        db.session.commit()
        
        return jsonify(doctor_schema.dump(new_doctor)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    doctor_data = request.json
    doctor = Doctor.query.filter_by(email=doctor_data.get('email')).first()

    if doctor and bcrypt.check_password_hash(doctor.password, doctor_data.get('password')):
        access_token = create_access_token(
            identity=str(doctor.id),
            expires_delta=timedelta(hours=12)
        )
        return jsonify({'doctor': doctor_schema.dump(doctor), 'token': access_token}), 200
    
    return jsonify({'error': 'Invalid email or password'}), 401