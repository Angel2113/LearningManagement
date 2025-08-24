from sqlalchemy.orm import Session
from app.models.Users import Users
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.password_hashing import hash_password
import uuid
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


def create_user(db: Session, user: UserCreate) -> dict:
    """
    Create a new user in the database. (CREATE)
    :param db: Database session
    :param user: User Schema
    :return: A dictionary with the result message
    """
    # Validate if the user already exists
    user_from_db = get_user(db=db, username = user.username)
    logger.info(f"User from db looking by username: {user_from_db}")
    if user_from_db: return {"message": "User already exists"}

    # Validate if the email already exists
    user_from_db = get_user(db=db, email = user.email)
    logger.info(f"User from db looking by email: {user_from_db}")
    if user_from_db: return {"message": "Email already exists"}

    # Validate if password matches the confirmation password
    if user.password != user.password_confirmation:
        return {"message": "Passwords do not match"}

    new_user = Users(
        id = str(uuid.uuid4()),
        username = user.username,
        email = user.email,
        password_hash = hash_password(user.password),
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User created successfully"}

def get_user(db: Session, user_id:str = None  ,username: str = None, email: str = None):
    """
    Get a user by username or email. (READ)
    :param db: Database session
    :param user_id: user id
    :param username: username
    :param email: email
    :return: Query result
    """
    if user_id:
        logger.info(f"Getting user by id: {user_id}")
        user = db.query(Users).filter(Users.id == user_id).first()
    if username:
        logger.info(f"Getting user by username: {username}")
        user = db.query(Users).filter(Users.username == username).first()
    if email:
        logger.info(f"Getting user by email: {email}")
        user = db.query(Users).filter(Users.email == email).first()
    return user if user else None

def get_all_users(db: Session):
    """
    Get all users. (READ)
    :param db: Database session
    :return:
    """
    users = db.query(Users).with_entities(Users.id, Users.username, Users.email, Users.role).all()
    return [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
            for user in users
        ]

def update_user(db: Session, user_id: str, updates: UserUpdate):
    """
    Update a user. (UPDATE)
    :param db: Database session
    :param user_id: User id
    :param updates: Parameters to update
    :return: a result message
    """
    user = get_user(db = db, user_id = user_id)
    if not user:
        return {"message": "User not found"}
    if updates.username:
        user.username = updates.username
    if updates.email:
        user.email = updates.email
    if updates.password:
        user.password_hash = hash_password(updates.password)
    if updates.role:
        user.role = updates.role
    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully"}

def delete_user(db: Session, user_id: str) -> dict:
    """
    Delete a user.
    :param db: Database session
    :param user_id: user id
    :return: a result message
    """
    user = get_user(db = db, user_id = user_id)
    if not user:
        return {"message": "User not found"}
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}