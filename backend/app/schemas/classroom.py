from sqlmodel import SQLModel
from app.schemas.department import DepartmentRead


class ClassroomBase(SQLModel):
    building_name: str
    room_no: str
    capacity: int
    department_id: int


class ClassroomCreate(ClassroomBase):
    pass


class ClassroomUpdate(SQLModel):
    building_name: str | None = None
    room_no: str | None = None
    capacity: int | None = None
    department_id: int | None = None


class ClassroomRead(SQLModel):
    id: int
    building_name: str
    room_no: str
    capacity: int
    department: DepartmentRead | None = None

    class Config:
        from_attributes = True


class DeleteClassroomResponse(SQLModel):
    message: str
    data: ClassroomRead | None = None
