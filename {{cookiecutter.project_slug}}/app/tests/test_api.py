from fastapi.testclient import TestClient

from app.api import fastapi_app

client = TestClient(fastapi_app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_run_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_load_docs():
    response = client.get("/docs")
    assert response.status_code == 200
