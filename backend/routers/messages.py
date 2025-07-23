from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import MessageCreate, Message
from database import SessionLocal
from services import messages_service

router = APIRouter(prefix="/api/messages", tags=["Messages"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return messages_service.create_message(db, message)

@router.get("/{message_id}", response_model=Message)
def get_message(message_id: int, db: Session = Depends(get_db)):
    return messages_service.get_message(db, message_id)
