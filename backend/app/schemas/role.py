from pydantic import BaseModel

class RoleCreate(BaseModel):
    role_name: str
    
class RoleRead(BaseModel):
    id: int
    role_name: str
    
    class Config:
        orm_mode = True