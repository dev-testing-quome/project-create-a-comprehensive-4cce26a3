from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str

class Appointment(BaseModel):
    id: int
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class Message(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class MedicalRecordCreate(BaseModel):
    patient_id: int
    document: str

class MedicalRecord(BaseModel):
    id: int
    patient_id: int
    document: str
    upload_date: datetime

    class Config:
        orm_mode = True

# Add schemas for Prescriptions and Billing as needed
