from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    year: int
    
    # Relationships
    classrooms: List["Classroom"] = Relationship(back_populates="department")
    faculties: List["Faculty"] = Relationship()
    subjects: List["Subject"] = Relationship()
