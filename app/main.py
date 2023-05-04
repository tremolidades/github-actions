import logging
from logging.config import dictConfig
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Settings, LogConfig
from app.api.endpoints import base

dictConfig(LogConfig().dict())
logger = logging.getLogger("base")
settings = Settings()

logger.debug("{} Main init".format(settings.PROJECT_NAME))

origins = [
    "http://localhost:4200",
    settings.ALLOWED_HOST
]

app = FastAPI(title=settings.PROJECT_NAME, version=settings.release, docs_url='{}/docs'.format(settings.API_STR),
              redoc_url='{}/redoc'.format(settings.API_STR), openapi_url='{}/openapi.json'.format(settings.API_STR))

app.include_router(base.router, prefix=settings.API_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
