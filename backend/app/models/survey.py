import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class SeismicSurvey(Base):
    __tablename__ = "seismic_surveys"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    survey_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    survey_type = Column(String(10), nullable=False)
    area_km2 = Column(Float, default=0)
    acquisition_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    status = Column(String(20), default="acquired")
    line_km = Column(Float, default=0)
    fold = Column(Integer, default=0)
    resolution_m = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
