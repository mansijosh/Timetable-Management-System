from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.crud.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=list[UserOut])
def get_users(session: Session = Depends(get_db), current_user=Depends(get_current_user)):
    statement = select(User)
    results = session.exec(statement).all()
    return results

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, session: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user.model_dump(exclude_unset=True)
    for field, value in user_data.items():
        setattr(db_user, field, value)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    session.delete(db_user)
    session.commit()
    return {"ok": True}
