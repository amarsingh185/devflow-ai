from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "DevFlow AI"


def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={
            "code": "def hello():\n    return 'Hello'"
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "hello" in response.json()["functions"]


def test_invalid_request():
    response = client.post(
        "/analyze",
        json={}
    )

    assert response.status_code == 422