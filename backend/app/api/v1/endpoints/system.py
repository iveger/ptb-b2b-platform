from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/info", tags=["system"])
def system_info():
    return {
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "env": settings.ENV,
        "debug": settings.DEBUG,
    }