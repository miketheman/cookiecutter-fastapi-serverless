"""
Any Pydantic models live here.
See: https://pydantic-docs.helpmanual.io/usage/models/
"""
from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "ok"
