from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import AppointmentCreate, Appointment
from database import SessionLocal
from services import appointments_service

router = APIRouter(prefix="/api/appointments", tags=["Appointments"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return appointments_service.create_appointment(db, appointment)

@router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointments_service.get_appointment(db, appointment_id)
