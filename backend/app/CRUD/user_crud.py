from sqlalchemy.orm import Session
from app.models.Users import Users
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.password_hashing import hash_password
import uuid


def create_user(db: Session, user: UserCreate) -> dict:
    """
    Create a new user in the database. (CREATE)
    :param db: Database session
    :param user: User Schema
    :return: A dictionary with the result message
    """
    if get_user(db = db, username = user.username, email = user.email):
        return {"message": "User already exists"}
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
    user = None
    if user_id:
        user = db.query(Users).filter(Users.id == user_id).first()
    if username:
        user = db.query(Users).filter(Users.username == username).first()
    if email:
        user = db.query(Users).filter(Users.email == email).first()
    if user:
        return user
    return {"message": "User not found"}

def get_all_users(db: Session):
    """
    Get all users. (READ)
    :param db: Database session
    :return:
    """
    return db.query(Users).all()

def update_user(db: Session, user_id: str, updates: UserUpdate):
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

def delete_user(db: Session, user_id: str):
    user = user = get_user(db = db, user_id = user_id)
    if not user:
        return {"message": "User not found"}
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}