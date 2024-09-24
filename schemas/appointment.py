from app import ma
from app.models import Appointment

class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)