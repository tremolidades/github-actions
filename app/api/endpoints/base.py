import logging
from fastapi import APIRouter
from app.schemas.info import InfoBase
from app.core.config import Settings

settings = Settings()
logger = logging.getLogger("base")
router = APIRouter()


@router.get("/info", tags=["base"], response_model=InfoBase)
async def infoView():
    logger.debug("Info View Called")
    return {"app_name": settings.PROJECT_NAME, "release": settings.release}
