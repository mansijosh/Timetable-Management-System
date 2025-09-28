# app/routes/department.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_db
from app.models.department import Department
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=Department)
def create_department(dept: Department, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Check if the same department name for the same year already exists
    existing = db.exec(
        select(Department).where(
            (Department.name == dept.name) & (Department.year == dept.year)
        )
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Department with this name and year already exists")
    
    db_dept = Department.model_validate(dept)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

@router.get("/", response_model=List[Department])
def get_departments(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    departments = db.exec(select(Department)).all()
    return departments
