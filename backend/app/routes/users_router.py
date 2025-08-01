from fastapi import APIRouter, Depends
from typing import Annotated
import app.CRUD.user_crud as u_crud
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session

users_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.get("/users/{username}", tags=["Users"])
async def get_user(username:str, db: Annotated[Session, Depends(get_db)]):
    user = u_crud.get_user(db, username)
    if user:
        return user
    else:
        return {"message": "User not found"}

@users_router.get("/all_users", tags=["Users"])
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    return u_crud.get_all_users(db)

@users_router.post("/users", tags=["Users"])
async def create_user(user: u_crud.UserCreate, db: Annotated[Session, Depends(get_db)]):
    return u_crud.create_user(
        db = db,
        user = user
    )

@users_router.put("/users/{user_id}", tags=["Users"])
async def update_user(user_id: str, updates: u_crud.UserUpdate, db: Annotated[Session, Depends(get_db)]):
    return u_crud.update_user(db = db, user_id = user_id, updates = updates)

@users_router.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: str, db: Annotated[Session, Depends(get_db)]):
    return u_crud.delete_user(db, user_id)