from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
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
