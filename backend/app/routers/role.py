from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_db
from app.schemas.role import RoleCreate, RoleRead, DeleteRoleResponse
from app.schemas.utils import DeleteResponse
from app.crud.role import create_role, get_roles, get_role_by_id, delete_role
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=RoleRead)
def add_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/", response_model=list[RoleRead])
def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)

@router.get("/{role_id}", response_model=RoleRead)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.delete("/{role_id}", response_model=DeleteRoleResponse)
def remove_role(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    role_public = RoleRead.model_validate(role)
    
    db.delete(role)
    db.commit()

    
    return DeleteRoleResponse(message="Role deleted successfully",
                          data = role_public)
    
    