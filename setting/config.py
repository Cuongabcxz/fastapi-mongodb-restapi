from typing import Optional
from pydantic import BaseSettings


class AppEnvConfig(BaseSettings):
    APP_PROJECT_NAME: str = "FastApi-App"
    APP_DEBUG: bool = True
    APP_DOCS_URL: Optional[str] = '/docs'

    APP_DB_MONGO_URI: str = "mongodb://localhost:27017"
    APP_DB_MONGO_NAME: str = "local"

    REDIS_URL: str = "redis://localhost:6379"
    REDIS_RESPONSE: bool = True
    REDIS_DB: int = 0

    BROKER_URL: str = "redis://172.27.230.25:6379/9"
    BACKEND_URL: str = "redis://172.27.230.25:6379/9"

    class Config:
        case_sensitive = True
        validate_assignment = True


settings = AppEnvConfig(_env_file='.env')
