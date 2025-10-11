# app/routers/profile.py

from fastapi import APIRouter, Depends
from app.models.user import User
from app.schemas.user import UserOut
from app.crud.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserOut)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user
