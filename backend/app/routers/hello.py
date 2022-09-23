from os import environ
from app.schemas import AddPayload

from fastapi import APIRouter, Depends
from app.config import Settings, get_settings

router = APIRouter(prefix='/hello')

@router.get("/")
def hello():
    return {"Hello": "World"}

@router.post("/add")
def add(body: AddPayload):
    return {"new_number": body.first_number + body.second_number}

@router.get("/env")
def get_env(settings: Settings = Depends(get_settings)):
    return {"env": settings.environment}