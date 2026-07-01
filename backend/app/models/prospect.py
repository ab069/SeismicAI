import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Prospect(Base):
    __tablename__ = "prospects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("seismic_surveys.id"), nullable=False)
    prospect_name = Column(String(255), nullable=False)
    volume_oil_mmboe = Column(Float, default=0)
    volume_gas_bcf = Column(Float, default=0)
    probability = Column(Float, default=0)
    risk_level = Column(String(10), default="medium")
    status = Column(String(20), default="lead")
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
