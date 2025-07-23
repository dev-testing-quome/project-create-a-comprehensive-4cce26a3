from sqlalchemy.orm import Session
from models import Appointment

def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(patient_id=1, provider_id=appointment.provider_id, date_time=appointment.date_time, description=appointment.description) #patient_id hardcoded for simplicity, should be replaced with user authentication
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()
