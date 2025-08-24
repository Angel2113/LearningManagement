from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

class CreateGoalSchema(BaseModel):
    description: str = Field(min_length=5, max_length=255)
    status: str = Field(min_length=2, max_length=20)
    eta: str = Field(min_length=2, max_length=20)
    resources: str = Field(min_length=5, max_length=255)
    target_date: date

class UpdateGoalSchema(BaseModel):
    description: Optional[str] = None
    status: Optional[str] = None
    eta: Optional[str] = None
    resources: Optional[str] = None
    target_date: Optional[date] = None