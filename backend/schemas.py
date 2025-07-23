from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserBase(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    datetime: datetime
    description: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class MedicalRecordBase(BaseModel):
    patient_id: int
    document: str

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecord(MedicalRecordBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class PrescriptionBase(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: Optional[str] = None

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class BillingRecordBase(BaseModel):
    patient_id: int
    amount: int
    description: str

class BillingRecordCreate(BillingRecordBase):
    pass

class BillingRecord(BillingRecordBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True