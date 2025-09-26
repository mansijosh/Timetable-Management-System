from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_db
from app.models.classroom import Classroom
from app.models.department import Department
from app.schemas.classroom import ClassroomCreate, ClassroomRead
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=ClassroomRead)
def create_classroom(classroom: ClassroomCreate, session: Session = Depends(get_db),current_user = Depends(get_current_user)):
    # Check if department exists
    department = session.get(Department, classroom.department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    db_classroom = Classroom.model_validate(classroom)
    session.add(db_classroom)
    session.commit()
    session.refresh(db_classroom)
    return db_classroom

@router.get("/", response_model=list[ClassroomRead])
def get_classrooms(session: Session = Depends(get_db),current_user = Depends(get_current_user)):
    statement = select(Classroom)
    results = session.exec(statement).all()
    return results
