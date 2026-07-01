from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import get_current_user


async def get_db_session(db: AsyncSession = Depends(get_db)):
    return db


async def get_authenticated_user(
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return {"user_id": user_id, "db": db}
