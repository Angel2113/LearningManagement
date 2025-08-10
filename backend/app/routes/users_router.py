from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.CRUD import user_crud
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.token_handler import decode_token
from app.routes.auth_router import get_current_user
from app.database import get_db

users_router = APIRouter()
user_depencency = Annotated[dict, Depends(get_current_user)]

@users_router.get("/users/{username}", tags=["Users"])
async def get_user(username: user_depencency, db: Session = Depends(get_db)):
    user = user_crud.get_user(db = db, username=username['username'])
    if user:
        return user
    else:
        return {"message": "User not found"}

@users_router.get("/all_users", tags=["Users"])
async def get_all_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)

@users_router.post("/users", tags=["Users"])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db = db, user = user)

@users_router.put("/users/{user_id}", tags=["Users"])
async def update_user(user_id: str, updates: UserUpdate, db: Session = Depends(get_db)):
    return user_crud.update_user(db = db, user_id = user_id, updates = updates)

@users_router.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    return user_crud.delete_user(db = db, user_id = user_id)