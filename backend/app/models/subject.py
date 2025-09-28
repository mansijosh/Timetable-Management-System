from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Subject(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    professor_id: int = Field(foreign_key="faculty.id")
    department_id: int = Field(foreign_key="department.id")
    
    # Relationships
    professor: Optional["Faculty"] = Relationship(back_populates="subjects")
    department: Optional["Department"] = Relationship()
