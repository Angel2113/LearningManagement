from ..database import Base
from sqlalchemy import Column, String, DateTime, Date, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import date
import uuid

class Goals(Base):
    __tablename__ = 'goals'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    title = Column(String(255))
    current_level = Column(String(255))
    resources = Column(String(255))
    target_date = Column(Date)
    days_per_week = Column(Integer)
    hours_per_day = Column(Integer)
    status= Column(String(20), default='new')
    created_at = Column(DateTime, default=date.today())
    ia_suggestion = Column(Text)
