from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, func

from app.database import get_db
from app.models.subject import Subject
from app.models.faculty import Faculty
from app.models.classroom import Classroom
from app.models.department import Department
from app.crud.deps import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])
@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # optional but recommended
):
    try:
        total_subjects = db.exec(select(func.count(Subject.id))).one()
        total_faculties = db.exec(select(func.count(Faculty.id))).one()
        total_classrooms = db.exec(select(func.count(Classroom.id))).one()
        total_departments = db.exec(select(func.count(Department.id))).one()

        return {
            "total_subjects": total_subjects,
            "total_faculties": total_faculties,
            "total_classrooms": total_classrooms,
            "total_departments": total_departments,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch dashboard statistics"
        )
