from sqlalchemy.orm import Session
from app.models.Users import Users
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.password_hashing import hash_password
from app.database import engine, SessionLocal
import uuid
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class CRUDUser:

    def __init__(self):
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()

    def create_user(self, user: UserCreate) -> dict:
        """
        Create a new user in the database. (CREATE)
        :param db: Database session
        :param user: User Schema
        :return: A dictionary with the result message
        """
        new_user = Users(
            id = str(uuid.uuid4()),
            username = user.username,
            email = user.email,
            password_hash = hash_password(user.password),
            role = user.role
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return {"message": f"User created successfully"}



    def get_user(self, user_id:str = None  ,username: str = None, email: str = None):
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
            logger.info(f"Getting user by id: {user_id}")
            user = self.db.query(Users).filter(Users.id == user_id).first()
        if username:
            logger.info(f"Getting user by username: {username}")
            user = self.db.query(Users).filter(Users.username == username).first()
        if email:
            logger.info(f"Getting user by email: {email}")
            user = self.db.query(Users).filter(Users.email == email).first()
        if user:
            return user
        return {"message": "User not found"}

    def get_all_users(self):
        """
        Get all users. (READ)
        :param db: Database session
        :return:
        """
        return self.db.query(Users).all()

    def update_user(self, user_id: str, updates: UserUpdate):
        user = self.get_user(user_id = user_id)
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
        self.db.commit()
        self.db.refresh(user)
        return {"message": "User updated successfully"}

    def delete_user(self, user_id: str):
        user = user = self.get_user(user_id = user_id)
        if not user:
            return {"message": "User not found"}
        self.db.delete(user)
        self.db.commit()
        return {"message": "User deleted successfully"}