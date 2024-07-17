from fastapi.testclient import TestClient

from app.main import app
from app.version import __version__

client = TestClient(app)


def test_root_main():
    response = client.get("/api/v1/ai-service-template/version")
    assert response.status_code == 200
    assert response.json() == {"version": __version__}
