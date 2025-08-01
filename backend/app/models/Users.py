import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password_hash = Column(String(255))
    role = Column(String(20), default='user')
    created_at = Column(DateTime, default=datetime.utcnow)
