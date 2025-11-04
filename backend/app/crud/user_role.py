from sqlmodel import Session, select
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleCreate

def create_user_role(db: Session, role_data: UserRoleCreate):
    new_role = UserRole.from_orm(role_data)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_user_roles(db: Session):
    return db.exec(select(UserRole)).all()

def get_roles_by_user_id(db: Session, user_id: int):
    return db.exec(select(UserRole).where(UserRole.user_id == user_id)).all()
