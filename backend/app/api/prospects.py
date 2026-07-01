from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.deps import get_authenticated_user
from app.schemas.prospect import ProspectCreate, ProspectResponse, ProspectStats
from app.services.prospect_service import create_prospect, get_prospects, get_prospects_by_survey, get_prospect, update_prospect, delete_prospect, get_prospect_stats

router = APIRouter(prefix="/prospects", tags=["prospects"])


@router.post("/", response_model=ProspectResponse)
async def create_prospect_endpoint(data: ProspectCreate, auth: dict = Depends(get_authenticated_user)):
    return await create_prospect(auth["db"], UUID(auth["user_id"]), data)


@router.get("/", response_model=list[ProspectResponse])
async def list_prospects(auth: dict = Depends(get_authenticated_user)):
    return await get_prospects(auth["db"], UUID(auth["user_id"]))


@router.get("/stats", response_model=ProspectStats)
async def prospect_stats(auth: dict = Depends(get_authenticated_user)):
    return await get_prospect_stats(auth["db"], UUID(auth["user_id"]))


@router.get("/survey/{survey_id}", response_model=list[ProspectResponse])
async def list_prospects_by_survey(survey_id: UUID, auth: dict = Depends(get_authenticated_user)):
    return await get_prospects_by_survey(auth["db"], survey_id)


@router.get("/{prospect_id}", response_model=ProspectResponse)
async def get_prospect_endpoint(prospect_id: UUID, auth: dict = Depends(get_authenticated_user)):
    prospect = await get_prospect(auth["db"], prospect_id)
    if not prospect:
        raise HTTPException(status_code=404, detail="Prospect not found")
    return prospect


@router.patch("/{prospect_id}", response_model=ProspectResponse)
async def update_prospect_endpoint(prospect_id: UUID, data: dict, auth: dict = Depends(get_authenticated_user)):
    prospect = await update_prospect(auth["db"], prospect_id, data)
    if not prospect:
        raise HTTPException(status_code=404, detail="Prospect not found")
    return prospect


@router.delete("/{prospect_id}")
async def delete_prospect_endpoint(prospect_id: UUID, auth: dict = Depends(get_authenticated_user)):
    deleted = await delete_prospect(auth["db"], prospect_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Prospect not found")
    return {"message": "Prospect deleted"}
