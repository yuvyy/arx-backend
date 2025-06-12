from app.schemas import user as userSchemas
from app.crud import user as userCrud
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.database import get_db


router = APIRouter(prefix='/user', tags=['user'])

@router.post('/register', response_model=userSchemas.UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: userSchemas.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    else:
        return userCrud.createUser(db, user)
