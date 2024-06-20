from sqlalchemy.orm import Session
from app.models import Role, Permission, RolePermission
from app.schemas import RoleCreate, PermissionCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def attach_permission_to_role(db: Session, role_id: int, permission: PermissionCreate):
    db_permission = Permission(name=permission.name)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    db_role_permission = RolePermission(role_id=role_id, permission_id=db_permission.id)
    db.add(db_role_permission)
    db.commit()
    db.refresh(db_role_permission)
    return db_role_permission