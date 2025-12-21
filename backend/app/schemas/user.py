# app/schemas/user.py
from pydantic import BaseModel, EmailStr, validator
import re

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: int | None = None

@validator("email")
def validate_domain(cls, v):
    pattern = r"^[a-zA-Z0-9._%+-]+@(gmail\.com|[a-zA-Z0-9-]+\.(com|in|org|net))$"
    if not re.match(pattern, v):
        raise ValueError("❌ Invalid email. Only Gmail or .com, .in, .org, .net domains are allowed")
    return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str
   
    
class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role_id: int | None = None

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role_id: int | None = None

    class Config:
        orm_mode = True
