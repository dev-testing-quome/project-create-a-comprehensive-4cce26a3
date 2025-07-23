from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import AppointmentCreate, Appointment
from ..models import Appointment as AppointmentModel

router = APIRouter(prefix="/api/appointments", tags=["Appointments"])

@router.post("", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = AppointmentModel(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Add other appointment-related routes (CRUD) as needed
