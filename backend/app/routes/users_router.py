from fastapi import APIRouter, Depends
from typing import Annotated
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from app.CRUD.user_crud import CRUDUser
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.token_handler import decode_token
from app.routes.auth_router import get_current_user

users_router = APIRouter()
user_crud = CRUDUser()
user_depencency = Annotated[dict, Depends(get_current_user)]

@users_router.get("/users/{username}", tags=["Users"])
async def get_user(username: user_depencency):
    user = user_crud.get_user(username=username['username'])
    if user:
        return user
    else:
        return {"message": "User not found"}

@users_router.get("/all_users", tags=["Users"])
async def get_all_users():
    return user_crud.get_all_users()

@users_router.post("/users", tags=["Users"])
async def create_user(user: UserCreate):
    return user_crud.create_user(user = user)

@users_router.put("/users/{user_id}", tags=["Users"])
async def update_user(user_id: str, updates: UserUpdate):
    return user_crud.update_user(user_id = user_id, updates = updates)

@users_router.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: str):
    return user_crud.delete_user(user_id)