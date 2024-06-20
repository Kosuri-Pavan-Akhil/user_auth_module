from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import RoleCreate, PermissionCreate
from app.services.roles import create_role, attach_permission_to_role
from app.utils.database import get_db

router = APIRouter(
    prefix="/roles",
    tags=["roles"],
)

@router.post("/")
def create_new_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.post("/{role_id}/permissions")
def add_permission_to_role(role_id: int, permission: PermissionCreate, db: Session = Depends(get_db)):
    return attach_permission_to_role(db, role_id, permission)