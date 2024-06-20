from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserLogin
from app.services.auth import register_user, authenticate_user
from app.utils.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = register_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already registered")
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user)
    if token is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}