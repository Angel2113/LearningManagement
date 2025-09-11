from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

class CreateGoalSchema(BaseModel):
    title: str = Field(min_length=5, max_length=255)
    current_level: Optional[str] = Field(min_length=2, max_length=20)
    resources: Optional[str] = Field(min_length=5, max_length=255)
    target_date: Optional[date]
    days_per_week: Optional[int]
    hours_per_day: Optional[int]
    status: Optional[str] = Field(min_length=2, max_length=20)

class UpdateGoalSchema(BaseModel):
    title: Optional[str] = Field(min_length=5, max_length=255)
    current_level: Optional[str] = Field(min_length=2, max_length=20)
    resources: Optional[str] = Field(min_length=5, max_length=255)
    target_date: Optional[date]
    days_per_week: Optional[int]
    hours_per_day: Optional[int]
    status: Optional[str] = Field(min_length=2, max_length=20)