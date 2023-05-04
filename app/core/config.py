import os
import secrets
from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    # ENV
    DATABASE_DB = os.environ.get('DATABASE_DB', 'postgres')
    DATABASE_USER = os.environ.get('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'postgres')
    DATABASE_HOST = os.environ.get('DATABASE_HOST', 'postgresdb')
    DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
    DATABASE_SSL = os.environ.get('DATABASE_SSL', 'disable')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')

    # GLOBAL
    API_STR: str = "/microservice/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    PROJECT_NAME: str = "Microservice API"
    ALLOWED_HOST = os.environ.get('ALLOWED_HOST', 'backend')
    release: str = "0.1.0"


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "base"
    LOG_FORMAT: str = "[%(asctime)s] [API] [%(levelprefix)s] %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "base": {"handlers": ["default"], "level": LOG_LEVEL},
    }


settings = Settings()
