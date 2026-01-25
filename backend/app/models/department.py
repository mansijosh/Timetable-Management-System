from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .classroom import Classroom
    from .faculty import Faculty
    from .subject import Subject


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    year: int

    # Relationships
    classrooms: List["Classroom"] = Relationship(back_populates="department")
    faculties: List["Faculty"] = Relationship()
    subjects: List["Subject"] = Relationship()
