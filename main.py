import os
from flask import Flask
from marshmallow.exceptions import ValidationError
from flask_migrate import Migrate

from init import db, ma, bcrypt, jwt, migrate
from controllers.auth_controller import auth_bp
from controllers.patient_controller import patients_bp
from controllers.doctor_controller import doctors_bp
from controllers.appointment_controller import appointments_bp
from controllers.department_controller import departments_bp

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    app.register_blueprint(auth_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(doctors_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(departments_bp)

    @app.route('/')
    def home():
        return {"message": "Welcome to MediTrack API"}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()