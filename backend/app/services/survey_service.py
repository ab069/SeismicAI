from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.survey import SeismicSurvey
from app.schemas.survey import SurveyCreate


async def create_survey(db: AsyncSession, user_id: UUID, data: SurveyCreate) -> SeismicSurvey:
    survey = SeismicSurvey(user_id=user_id, **data.model_dump())
    db.add(survey)
    await db.commit()
    await db.refresh(survey)
    return survey


async def get_surveys(db: AsyncSession, user_id: UUID) -> list[SeismicSurvey]:
    result = await db.execute(
        select(SeismicSurvey).where(SeismicSurvey.user_id == user_id).order_by(SeismicSurvey.created_at.desc())
    )
    return result.scalars().all()


async def get_survey(db: AsyncSession, survey_id: UUID) -> SeismicSurvey | None:
    result = await db.execute(select(SeismicSurvey).where(SeismicSurvey.id == survey_id))
    return result.scalar_one_or_none()


async def update_survey_status(db: AsyncSession, survey_id: UUID, status: str) -> SeismicSurvey | None:
    survey = await get_survey(db, survey_id)
    if survey:
        survey.status = status
        await db.commit()
        await db.refresh(survey)
    return survey


async def delete_survey(db: AsyncSession, survey_id: UUID) -> bool:
    survey = await get_survey(db, survey_id)
    if survey:
        await db.delete(survey)
        await db.commit()
        return True
    return False


async def get_survey_stats(db: AsyncSession, user_id: UUID) -> dict:
    total = await db.execute(select(func.count(SeismicSurvey.id)).where(SeismicSurvey.user_id == user_id))
    total_surveys = total.scalar() or 0

    area = await db.execute(select(func.coalesce(func.sum(SeismicSurvey.area_km2), 0)).where(SeismicSurvey.user_id == user_id))
    total_area = float(area.scalar() or 0)

    interp = await db.execute(
        select(func.count(SeismicSurvey.id)).where(SeismicSurvey.user_id == user_id, SeismicSurvey.status == "interpreting")
    )
    interpreting_count = interp.scalar() or 0

    return {"total_surveys": total_surveys, "total_area_km2": round(total_area, 2), "interpreting_count": interpreting_count}
