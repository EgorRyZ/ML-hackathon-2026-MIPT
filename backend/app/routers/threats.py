from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_threats():
    return [
        {"code": "UBI.190", "name": "Угроза BIOS", "description": "..."},
        {"code": "UBI.152", "name": "Сетевая атака", "description": "..."},
    ]