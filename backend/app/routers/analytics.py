from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
async def get_summary():
    return {
        "total_incidents": 2000,
        "successful_incidents": 800,
        "success_rate": 0.4,
        "unique_threats": 227,
        "unique_regions": 85,
        "unique_enterprises": 1500,
        "avg_host_count": 120.5,
    }