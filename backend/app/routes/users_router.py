from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.CRUD import user_crud
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.token_handler import decode_token
from app.routes.auth_router import get_current_user, security
from app.database import get_db
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

users_router = APIRouter()
user_depencency = Annotated[dict, Depends(get_current_user)]

@users_router.get("/user/{username}", tags=["Users"], dependencies=[Depends(security)])
async def get_user(username: user_depencency, db: Session = Depends(get_db)):
    """
    Get user by username (READ)
    :param username: Username
    :param db: Database session
    :return: return the user
    """
    user = user_crud.get_user(db = db, username=username['username'])
    if user:
        return user
    else:
        return {"message": "User not found"}

@users_router.get("/all_users", tags=["Users"], dependencies=[Depends(security)])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Get all users (READ)
    :param db: Database session
    :return: A list of all users
    """
    return user_crud.get_all_users(db)

@users_router.post("/user", tags=["Users"], dependencies=[Depends(security)])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user (CREATE)
    :param user: User Schema
    :param db: Database session
    :return: A result message
    """
    return user_crud.create_user(db = db, user = user)

@users_router.put("/user/{user_id}", tags=["Users"], dependencies=[Depends(security)])
async def update_user(user_id: str, updates: UserUpdate, db: Session = Depends(get_db)):
    """
    Update a user (UPDATE)
    :param user_id: User id to be updated
    :param updates: Parameters to update
    :param db: Database session
    :return: A result message
    """
    return user_crud.update_user(db = db, user_id = user_id, updates = updates)

@users_router.delete("/user/{user_id}", tags=["Users"], dependencies=[Depends(security)])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    """
    Delete a user (DELETE)
    :param user_id: User id to be deleted
    :param db: Database session
    :return: A result message
    """
    return user_crud.delete_user(db = db, user_id = user_id)