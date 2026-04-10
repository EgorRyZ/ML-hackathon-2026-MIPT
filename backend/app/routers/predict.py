from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.prediction import PredictRequest, PredictResponse

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest, db: Session = Depends(get_db)):
    # Заглушка MVP
    return PredictResponse(
        request_id="dummy",
        model_version="v1",
        inference_time_ms=50.0,
        incident_prediction={
            "will_happen": True,
            "probability": 0.73,
            "confidence_level": "high",
            "confidence_label": "High"
        },
        attack_time_prediction=None,
        threat_prediction=None,
        target_object_prediction=None,
        vulnerability_assessment=None,
        recommendations=[],
        explanations=None,
        business_impact=None
    )