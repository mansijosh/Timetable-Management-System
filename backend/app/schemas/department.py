from sqlmodel import SQLModel


class DepartmentBase(SQLModel):
    name: str
    year: int


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(SQLModel):
    name: str | None = None
    year: int | None = None


class DepartmentRead(SQLModel):
    id: int
    name: str
    year: int

    class Config:
        from_attributes = True


class DeleteDepartmentResponse(SQLModel):
    message: str
    data: DepartmentRead | None = None
