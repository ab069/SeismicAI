from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.prospect import Prospect
from app.schemas.prospect import ProspectCreate


async def create_prospect(db: AsyncSession, user_id: UUID, data: ProspectCreate) -> Prospect:
    prospect = Prospect(user_id=user_id, **data.model_dump())
    db.add(prospect)
    await db.commit()
    await db.refresh(prospect)
    return prospect


async def get_prospects(db: AsyncSession, user_id: UUID) -> list[Prospect]:
    result = await db.execute(
        select(Prospect).where(Prospect.user_id == user_id).order_by(Prospect.created_at.desc())
    )
    return result.scalars().all()


async def get_prospects_by_survey(db: AsyncSession, survey_id: UUID) -> list[Prospect]:
    result = await db.execute(
        select(Prospect).where(Prospect.survey_id == survey_id).order_by(Prospect.created_at.desc())
    )
    return result.scalars().all()


async def get_prospect(db: AsyncSession, prospect_id: UUID) -> Prospect | None:
    result = await db.execute(select(Prospect).where(Prospect.id == prospect_id))
    return result.scalar_one_or_none()


async def update_prospect(db: AsyncSession, prospect_id: UUID, data: dict) -> Prospect | None:
    prospect = await get_prospect(db, prospect_id)
    if prospect:
        for key, value in data.items():
            setattr(prospect, key, value)
        await db.commit()
        await db.refresh(prospect)
    return prospect


async def delete_prospect(db: AsyncSession, prospect_id: UUID) -> bool:
    prospect = await get_prospect(db, prospect_id)
    if prospect:
        await db.delete(prospect)
        await db.commit()
        return True
    return False


async def get_prospect_stats(db: AsyncSession, user_id: UUID) -> dict:
    total = await db.execute(select(func.count(Prospect.id)).where(Prospect.user_id == user_id))
    total_prospects = total.scalar() or 0

    drill = await db.execute(
        select(func.count(Prospect.id)).where(Prospect.user_id == user_id, Prospect.status == "drill_ready")
    )
    drill_ready = drill.scalar() or 0

    avg = await db.execute(select(func.coalesce(func.avg(Prospect.probability), 0)).where(Prospect.user_id == user_id))
    avg_probability = round(float(avg.scalar() or 0), 2)

    return {"total_prospects": total_prospects, "drill_ready": drill_ready, "avg_probability": avg_probability}
