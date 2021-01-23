from app.models import HealthCheck


def test_healthcheck_model():
    """A simple test to exercise a model with default properties."""
    assert HealthCheck().status == "ok"
    assert HealthCheck(status="broken").status == "broken"
