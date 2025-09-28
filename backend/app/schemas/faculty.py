from typing import Optional
from sqlmodel import SQLModel
from app.schemas.department import DepartmentRead

class FacultyBase(SQLModel):
    name: str
    department_id: int

class FacultyCreate(FacultyBase):
    pass

class FacultyUpdate(SQLModel):
    name: Optional[str] = None
    department_id: Optional[int] = None

class FacultyRead(SQLModel):
    id: int
    name: str
    department_id: int
    department: Optional[DepartmentRead] = None

    model_config = {"from_attributes": True}
