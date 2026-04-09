import numpy as np
from app.ml.loader import load_model
from app.ml.feature_builder import build_features
from app.schemas.prediction import PredictResponse, IncidentPrediction

class PredictionService:
    def __init__(self, db):
        self.db = db
        self.model = load_model("incident_classifier")

    def predict(self, request):
        features = build_features(request, self.db)
        proba = self.model.predict_proba(features)[0][1]
        will_happen = proba >= 0.5
        confidence = "high" if abs(proba - 0.5) > 0.3 else "medium"

        # Заглушки для остальных полей (MVP)
        return PredictResponse(
            request_id="mock-request-id",
            model_version="v1",
            inference_time_ms=42.0,
            incident_prediction=IncidentPrediction(
                will_happen=will_happen,
                probability=proba,
                confidence_level=confidence,
                confidence_label=confidence.capitalize()
            ),
            attack_time_prediction=None,
            threat_prediction=None,
            target_object_prediction=None,
            vulnerability_assessment=None,
            recommendations=[],
            explanations=None,
            business_impact=None
        )