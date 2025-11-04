from typing import Optional
from sqlmodel import SQLModel

class UserRoleCreate(SQLModel):
    user_id: int
    role_name: str

class UserRoleRead(SQLModel):
    id: int
    user_id: int
    role_name: str
