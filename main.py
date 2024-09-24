from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # JWT'yi uygulama ile ilişkilendirme
    JWTManager(app)

    # CORS ayarları
    CORS(app)

    # Route'ları içe aktarma
    from app.routes import patient, doctor, appointment, department, auth

    # Route'ları uygulamaya ekleme
    app.register_blueprint(patient.patient_bp, url_prefix='/api/patients')
    app.register_blueprint(doctor.doctor_bp, url_prefix='/api/doctors')
    app.register_blueprint(appointment.appointment_bp, url_prefix='/api/appointments')
    app.register_blueprint(department.department_bp, url_prefix='/api/departments')
    app.register_blueprint(auth.auth_bp, url_prefix='/api/auth')

    @app.route('/')
    def root():
        return {"message": "Welcome to MediTrack API"}

    return app

# Bu kısım, bu dosyayı doğrudan çalıştırdığımızda uygulamayı başlatır
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)