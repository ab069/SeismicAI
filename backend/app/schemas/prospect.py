from datetime import datetime

from pydantic import BaseModel


class ProspectCreate(BaseModel):
    survey_id: str
    prospect_name: str
    volume_oil_mmboe: float = 0
    volume_gas_bcf: float = 0
    probability: float = 0
    risk_level: str = "medium"
    status: str = "lead"


class ProspectResponse(BaseModel):
    id: str
    user_id: str
    survey_id: str
    prospect_name: str
    volume_oil_mmboe: float
    volume_gas_bcf: float
    probability: float
    risk_level: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class ProspectStats(BaseModel):
    total_prospects: int
    drill_ready: int
    avg_probability: float
