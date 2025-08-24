from ..database import Base
from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import date
import uuid

class Goals(Base):
    __tablename__ = 'goals'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    description = Column(String(255))
    status = Column(String(20), default='pending')
    eta = Column(String(20))
    resources = Column(String(255))
    target_date = Column(Date)
    created_at = Column(DateTime, default=date.today())