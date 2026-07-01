from datetime import datetime

from pydantic import BaseModel


class HorizonResponse(BaseModel):
    id: str
    user_id: str
    survey_id: str
    horizon_name: str
    depth_m: float
    amplitude: float
    continuity: int
    formation: str
    confidence: str
    created_at: datetime

    class Config:
        from_attributes = True
