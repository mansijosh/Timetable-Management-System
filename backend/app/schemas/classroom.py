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

class ClassroomUpdate(SQLModel):
    building_name: Optional[str] = None
    room_no: Optional[str] = None
    capacity: Optional[int] = None
    department_id: Optional[int] = None

class ClassroomRead(SQLModel):
    id: int
    building_name: str
    room_no: str
    capacity: int
    department: Optional[Department] = None

    model_config = {"from_attributes": True}
