from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.models import Doctor
from app.utils import check_password

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    doctor = Doctor.query.filter_by(email=email).first()
    if doctor and check_password(doctor.hashed_password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad email or password"}), 401