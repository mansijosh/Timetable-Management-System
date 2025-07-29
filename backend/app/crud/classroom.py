from pydantic import BaseModel, Field

class ClassroomBase(BaseModel):
    building_name: str = Field(..., example="Building A")
    room_number: str = Field(..., example="101")
    capacity: int = Field(..., example=60)

class ClassroomCreate(ClassroomBase):
    pass

class Classroom(ClassroomBase):
    class_id: int

    class Config:
        from_attributes = True
