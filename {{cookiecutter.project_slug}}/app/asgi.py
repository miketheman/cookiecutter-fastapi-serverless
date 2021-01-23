"""
ASGI wrapper for AWS API Gateway integration, using https://mangum.io
"""

from mangum import Mangum

from app.api import fastapi_app

handler = Mangum(fastapi_app)
