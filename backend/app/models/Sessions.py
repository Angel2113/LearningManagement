from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

class Sessions(Base):
    __tablename__ = 'sessions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_no = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(String(255), nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    goal_id = Column(UUID(as_uuid=True), nullable=False)
