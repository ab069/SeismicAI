from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.deps import get_authenticated_user
from app.schemas.horizon import HorizonResponse
from app.services.survey_service import get_survey

router = APIRouter(prefix="/horizons", tags=["horizons"])


@router.get("/survey/{survey_id}", response_model=list[HorizonResponse])
async def list_horizons_by_survey(survey_id: UUID, auth: dict = Depends(get_authenticated_user)):
    survey = await get_survey(auth["db"], survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    # Placeholder: return empty list; extend with horizon service as needed
    return []
