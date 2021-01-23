# from typing import Optional

from fastapi import FastAPI

from app.config import settings
from app.models import HealthCheck

fastapi_app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)


@fastapi_app.get("/")
def read_root():
    return {"Hello": "World"}


@fastapi_app.get("/healthz")
def run_health_check():
    return HealthCheck()
