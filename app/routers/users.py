from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.users import get_users, get_user_profile, assign_role_to_user
from app.utils.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/profile")
def read_user_profile(db: Session = Depends(get_db)):
    return get_user_profile(db)

@router.post("/{user_id}/roles")
def assign_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    return assign_role_to_user(db, user_id, role_id)