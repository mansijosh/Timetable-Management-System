from typing import Optional
from sqlmodel import SQLModel
from app.models.department import Department

class ClassroomBase(SQLModel):
    building_name: str
    room_no: str
    capacity: int
    department_id: int

class ClassroomCreate(ClassroomBase):
    pass

class ClassroomRead(ClassroomBase):
    id: int
    department: Optional[Department]

    class Config:
        from_attributes = True
