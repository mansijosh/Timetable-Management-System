from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from .department import Department
    from .subject import Subject


class Faculty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    department_id: int = Field(foreign_key="department.id")

    # Relationships
    department: Optional["Department"] = Relationship()
    subjects: List["Subject"] = Relationship()
