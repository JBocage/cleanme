from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    environment: str = "dev"

@lru_cache
def get_settings() -> BaseSettings:
    return Settings()