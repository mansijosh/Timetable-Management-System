from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.subject import Subject


class Faculty(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    department_id: int = Field(foreign_key="department.id")

    # Relationships
    department: "Department | None" = Relationship()
    subjects: list["Subject"] = Relationship()
