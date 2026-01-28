from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.classroom import Classroom
    from app.models.faculty import Faculty
    from app.models.subject import Subject


class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    year: int

    # Relationships
    classrooms: list["Classroom"] = Relationship(back_populates="department")
    faculties: list["Faculty"] = Relationship()
    subjects: list["Subject"] = Relationship()
