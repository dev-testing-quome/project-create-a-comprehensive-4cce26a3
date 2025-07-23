from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import MedicalRecordCreate, MedicalRecord
from ..models import MedicalRecord as MedicalRecordModel

router = APIRouter(prefix="/api/medical_records", tags=["Medical Records"])

@router.post("", response_model=MedicalRecord)
def create_medical_record(medical_record: MedicalRecordCreate, db: Session = Depends(get_db)):
    db_medical_record = MedicalRecordModel(**medical_record.dict())
    db.add(db_medical_record)
    db.commit()
    db.refresh(db_medical_record)
    return db_medical_record

# Add other medical record-related routes (CRUD) as needed
