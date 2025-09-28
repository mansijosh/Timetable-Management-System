from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.database import get_db
from app.models.subject import Subject
from app.models.faculty import Faculty
from app.models.department import Department
from app.schemas.subject import SubjectCreate, SubjectRead, SubjectUpdate
from app.crud.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=SubjectRead)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    if not db.get(Faculty, subject.professor_id):
        raise HTTPException(status_code=404, detail="Faculty not found")
    if not db.get(Department, subject.department_id):
        raise HTTPException(status_code=404, detail="Department not found")
    db_subject = Subject.model_validate(subject)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.get("/", response_model=List[SubjectRead])
def get_subjects(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.exec(select(Subject)).all()

@router.get("/{subject_id}", response_model=SubjectRead)
def get_subject_by_id(subject_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_subject = db.get(Subject, subject_id)
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

@router.put("/{subject_id}", response_model=SubjectRead)
def update_subject(subject_id: int, subject: SubjectUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_subject = db.get(Subject, subject_id)
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    subject_data = subject.model_dump(exclude_unset=True)
    
    # Ensure faculty exists if changed
    if "professor_id" in subject_data:
        if not db.get(Faculty, subject_data["professor_id"]):
            raise HTTPException(status_code=404, detail="Faculty not found")
    
    # Ensure department exists if changed
    if "department_id" in subject_data:
        if not db.get(Department, subject_data["department_id"]):
            raise HTTPException(status_code=404, detail="Department not found")
    
    for field, value in subject_data.items():
        setattr(db_subject, field, value)
    
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.delete("/{subject_id}")
def delete_subject(subject_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_subject = db.get(Subject, subject_id)
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(db_subject)
    db.commit()
    return {"ok": True}
