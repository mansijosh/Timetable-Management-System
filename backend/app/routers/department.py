# app/routes/department.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_db
from app.models.department import Department
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=Department)
def create_department(dept: Department, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    # Optional: Check if already exists
    existing = db.exec(select(Department).where(Department.name == dept.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Department already exists")
    
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept

@router.get("/", response_model=List[Department])
def get_departments(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    departments = db.exec(select(Department)).all()
    return departments

@router.get("/{department_id}", response_model=Department)
def get_department_by_id(department_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    dept = db.get(Department, department_id)
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

@router.put("/{department_id}", response_model=Department)
def update_department(department_id: int, dept: Department, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.get(Department, department_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Department not found")
    # Only update fields that are provided
    if dept.name is not None:
        existing.name = dept.name
    if dept.year is not None:
        existing.year = dept.year
    db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.get(Department, department_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(existing)
    db.commit()
    return {"ok": True}