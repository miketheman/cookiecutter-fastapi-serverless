from mangum import Mangum

from app.asgi import handler


def test_handler():
    assert isinstance(handler, Mangum)
