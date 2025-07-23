from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, password=hashed_password, email=user.email, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user.first_name:
            db_user.first_name = user.first_name
        if user.last_name:
            db_user.last_name = user.last_name
        if user.email:
            db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user
