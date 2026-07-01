from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db_session
from app.schemas.user import UserRegister, UserLogin, TokenResponse
from app.services.auth import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(data: UserRegister, db: AsyncSession = Depends(get_db_session)):
    try:
        return await register_user(db, data.email, data.password, data.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(data: UserLogin, db: AsyncSession = Depends(get_db_session)):
    try:
        return await login_user(db, data.email, data.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
