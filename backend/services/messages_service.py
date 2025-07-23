from sqlalchemy.orm import Session
from models import Message

def create_message(db: Session, message: MessageCreate):
    db_message = Message(sender_id=1, recipient_id=message.recipient_id, content=message.content) #sender_id hardcoded, replace with authentication
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_message(db: Session, message_id: int):
    return db.query(Message).filter(Message.id == message_id).first()
