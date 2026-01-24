from sqlmodel import SQLModel

class Message(SQLModel):
    message: str
    
class DeleteResponse(SQLModel):
    message: str
    data: dict| None = None
