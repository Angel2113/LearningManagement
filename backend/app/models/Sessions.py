from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Sessions(Base):
    __tablename__ = 'sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    task = Column(String(255))
    duration = Column(Integer)
    focus_level = Column(String(20))
    notes = Column(Text)
    create_at = Column(DateTime)