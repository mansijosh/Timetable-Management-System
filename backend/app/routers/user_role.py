from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_db
from app.crud import user_role as crud
from app.schemas.user_role import UserRoleCreate, UserRoleRead

router = APIRouter(prefix="/roles", tags=["User Roles"])

@router.post("/", response_model=UserRoleRead)
def create_role(role_data: UserRoleCreate, db: Session = Depends(get_db)):
    return crud.create_user_role(db, role_data)

@router.get("/", response_model=list[UserRoleRead])
def list_roles(db: Session = Depends(get_db)):
    return crud.get_user_roles(db)

@router.get("/user/{user_id}", response_model=list[UserRoleRead])
def get_user_roles(user_id: int, db: Session = Depends(get_db)):
    return crud.get_roles_by_user_id(db, user_id)
