from sqlmodel import SQLModel
from app.schemas.department import DepartmentRead
from app.schemas.faculty import FacultyRead


class SubjectBase(SQLModel):
    name: str
    faculty_id: int
    department_id: int


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SQLModel):
    name: str | None = None
    faculty_id: int | None = None
    department_id: int | None = None


class SubjectRead(SQLModel):
    id: int
    name: str
    faculty: FacultyRead | None = None
    department: DepartmentRead | None = None


class DeleteSubjectResponse(SQLModel):
    message: str
    data: SubjectRead | None = None

    class Config:
        from_attributes = True
