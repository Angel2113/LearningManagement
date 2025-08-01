from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    """
        Schema for creating a new user
    """
    username: str = Field(min_length=5, max_length=50)
    email: EmailStr = Field(min_length=5, max_length=50)
    password: str = Field(min_length=8, max_length=255)
    role: str = Field(min_length=2, max_length=20)

class UserRead(BaseModel):
    """
        Schema for reading a user
    """
    id: UUID
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    """
        Schema for updating a user
    """
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None

class UserDelete(BaseModel):
    """
        Shema for deleting a user
    """
    id: UUID