from datetime import datetime

from pydantic import BaseModel


class SurveyCreate(BaseModel):
    survey_name: str
    location: str
    survey_type: str
    area_km2: float = 0
    line_km: float = 0
    fold: int = 0
    resolution_m: float = 0


class SurveyResponse(BaseModel):
    id: str
    user_id: str
    survey_name: str
    location: str
    survey_type: str
    area_km2: float
    acquisition_date: datetime
    status: str
    line_km: float
    fold: int
    resolution_m: float
    created_at: datetime

    class Config:
        from_attributes = True


class SurveyStats(BaseModel):
    total_surveys: int
    total_area_km2: float
    interpreting_count: int
