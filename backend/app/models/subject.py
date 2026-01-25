from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .department import Department
    from .faculty import Faculty


class Subject(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    faculty_id: int = Field(foreign_key="faculty.id")
    department_id: int = Field(foreign_key="department.id")

    # Relationships
    faculty: Optional["Faculty"] = Relationship()
    department: Optional["Department"] = Relationship()
