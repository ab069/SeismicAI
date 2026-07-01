from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.deps import get_authenticated_user
from app.schemas.survey import SurveyCreate, SurveyResponse, SurveyStats
from app.services.survey_service import create_survey, get_surveys, get_survey, update_survey_status, delete_survey, get_survey_stats

router = APIRouter(prefix="/surveys", tags=["surveys"])


@router.post("/", response_model=SurveyResponse)
async def create_survey_endpoint(data: SurveyCreate, auth: dict = Depends(get_authenticated_user)):
    return await create_survey(auth["db"], UUID(auth["user_id"]), data)


@router.get("/", response_model=list[SurveyResponse])
async def list_surveys(auth: dict = Depends(get_authenticated_user)):
    return await get_surveys(auth["db"], UUID(auth["user_id"]))


@router.get("/stats", response_model=SurveyStats)
async def survey_stats(auth: dict = Depends(get_authenticated_user)):
    return await get_survey_stats(auth["db"], UUID(auth["user_id"]))


@router.get("/{survey_id}", response_model=SurveyResponse)
async def get_survey_endpoint(survey_id: UUID, auth: dict = Depends(get_authenticated_user)):
    survey = await get_survey(auth["db"], survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.patch("/{survey_id}/status", response_model=SurveyResponse)
async def update_status(survey_id: UUID, status: str, auth: dict = Depends(get_authenticated_user)):
    survey = await update_survey_status(auth["db"], survey_id, status)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.delete("/{survey_id}")
async def delete_survey_endpoint(survey_id: UUID, auth: dict = Depends(get_authenticated_user)):
    deleted = await delete_survey(auth["db"], survey_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Survey not found")
    return {"message": "Survey deleted"}
