from sqlmodel import SQLModel
from app.schemas.department import DepartmentRead


class FacultyBase(SQLModel):
    name: str
    department_id: int


class FacultyCreate(FacultyBase):
    pass


class FacultyUpdate(SQLModel):
    name: str | None = None
    department_id: int | None = None


class FacultyRead(SQLModel):
    id: int
    name: str
    department: DepartmentRead | None = None

    class Config:
        from_attributes = True


class DeleteFacultyResponse(SQLModel):
    message: str
    data: FacultyRead | None = None
