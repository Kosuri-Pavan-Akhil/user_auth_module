from sqlalchemy.orm import Session
from app.models import User, UserRole, Role

def get_users(db: Session):
    return db.query(User).all()

def get_user_profile(db: Session):
    # Assuming that user information is stored in the session or passed as a token
    return {"msg": "User profile"}

def assign_role_to_user(db: Session, user_id: int, role_id: int):
    db_user_role = UserRole(user_id=user_id, role_id=role_id)
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role