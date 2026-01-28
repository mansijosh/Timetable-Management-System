# app/models/user.py
from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .roles import Role


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    phone_number: str | None = Field(default=None, index=True)
    hashed_password: str

    role_id: int | None = Field(default=None, foreign_key="roles.id")
    role: "Role" = Relationship(back_populates="users")
