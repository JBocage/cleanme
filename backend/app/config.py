import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """The settings for the app"""

    environment: str = os.getenv("ENVIRONMENT", "dev")

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> BaseSettings:
    """Returns the app settings"""
    return Settings()
