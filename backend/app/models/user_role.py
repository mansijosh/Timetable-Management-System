# app/models/user_role.py
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class UserRole(SQLModel, table=True):
    __tablename__ = "user_roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")

    user: Optional["User"] = Relationship(back_populates="roles")
