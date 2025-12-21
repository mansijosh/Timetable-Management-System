from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    
class RoleRead(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True