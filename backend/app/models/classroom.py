from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.department import Department


class Classroom(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    building_name: str
    room_no: str
    capacity: int
    department_id: int = Field(foreign_key="department.id")
    department: "Department" = Relationship(back_populates="classrooms")
