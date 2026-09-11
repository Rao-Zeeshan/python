import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config.update({"TESTING": True})
    with flask_app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Python Flask App" in response.data


def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_greet(client):
    response = client.get("/api/greet/Zeeshan")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, Zeeshan!"


def test_echo(client):
    response = client.post("/api/echo", json={"key": "value"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["you_sent"] == {"key": "value"}


def test_echo_empty_body(client):
    response = client.post("/api/echo")
    assert response.status_code == 200
    data = response.get_json()
    assert data["you_sent"] == {}
