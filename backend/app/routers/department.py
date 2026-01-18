# app/routes/department.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_db
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentRead, DepartmentUpdate
from app.schemas.utils import DeleteResponse
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=DepartmentRead)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    # Optional: Check if already exists
    existing = db.exec(select(Department).where(Department.name == dept.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Department with this name and year already exists")
    
    db_dept = Department.model_validate(dept)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

@router.get("/", response_model=List[DepartmentRead])
def get_departments(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    departments = db.exec(select(Department)).all()
    return departments

@router.get("/{department_id}", response_model=DepartmentRead)
def get_department_by_id(department_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    dept = db.get(Department, department_id)
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

@router.put("/{department_id}", response_model=DepartmentRead)
def update_department(department_id: int, dept: DepartmentUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.get(Department, department_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Department not found")
    
    dept_data = dept.model_dump(exclude_unset=True)
    for field, value in dept_data.items():
        setattr(existing, field, value)
    
    db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{department_id}", response_model = DeleteResponse)
def delete_department(department_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.get(Department, department_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(existing)
    db.commit()
    return DeleteResponse(message="Department deleted successfully",
                            data = {
                                    "id" : existing.id,
                                    "name": existing.name,
                                    "year": existing.year
                            }
    )
