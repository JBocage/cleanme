from app.routers import main
from fastapi import FastAPI


def create_app() -> FastAPI:
    """Builds the app and returns it"""
    app = FastAPI()
    app.include_router(main.application.router)
    return app
