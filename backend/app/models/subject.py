from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.faculty import Faculty


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    faculty_id: int = Field(foreign_key="faculty.id")
    department_id: int = Field(foreign_key="department.id")

    # Relationships
    faculty: "Faculty | None" = Relationship()
    department: "Department | None" = Relationship()
