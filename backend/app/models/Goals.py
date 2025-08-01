from ..database import Base
from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Goals(Base):
    __tablename__ = 'goals'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    description = Column(String(255))
    status = Column(String(20), default='pending')
    target_date = Column(Date)
    create_at = Column(DateTime)