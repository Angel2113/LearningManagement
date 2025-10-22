from typing import Optional
from pydantic import BaseModel, Field
import uuid


class CreateSessionSchema(BaseModel):
    session_no: int
    title: str = Field(min_length=5, max_length=255)
    content: str
    status: Optional[str] = Field(min_length=2, max_length=20)
    user_id: uuid.UUID
    goal_id: uuid.UUID

