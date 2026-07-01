import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Horizon(Base):
    __tablename__ = "horizons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("seismic_surveys.id"), nullable=False)
    horizon_name = Column(String(255), nullable=False)
    depth_m = Column(Float, default=0)
    amplitude = Column(Float, default=0)
    continuity = Column(Integer, default=0)
    formation = Column(String(255), default="")
    confidence = Column(String(20), default="medium")
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
