from sqlmodel import Session, select
from app.models.roles import Role
from app.schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(role_name=role.role_name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    return db.exec(select(Role)).all()

def get_role_by_id(db: Session, role_id: int):
    return db.get(Role, role_id)

def delete_role(db: Session, role_id: int):
    role = db.get(Role, role_id)
    if role:
        db.delete(role)
        db.commit()
    return role
