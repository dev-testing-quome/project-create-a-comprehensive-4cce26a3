from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import MessageCreate, Message
from ..models import Message as MessageModel

router = APIRouter(prefix="/api/messages", tags=["Messages"])

@router.post("", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = MessageModel(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Add other message-related routes (CRUD) as needed
