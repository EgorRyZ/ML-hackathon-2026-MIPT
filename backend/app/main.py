from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, analytics, predict, threats
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ML Inference Service", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1/analytics")
app.include_router(predict.router, prefix="/api/v1")
app.include_router(threats.router, prefix="/api/v1/threats")