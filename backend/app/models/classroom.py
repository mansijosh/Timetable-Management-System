from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .department import Department

class Classroom(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    building_name: str
    room_no: str
    capacity: int
    department_id: int = Field(foreign_key="department.id")

    department: Department|None = Relationship()
