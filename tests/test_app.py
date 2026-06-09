import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint_returns_200(client):
    response = client.get("/api/health")
    assert response.status_code == 200


def test_health_endpoint_returns_healthy_status(client):
    response = client.get("/api/health")
    data = response.get_json()
    assert data["status"] == "healthy"


def test_health_endpoint_contains_required_fields(client):
    response = client.get("/api/health")
    data = response.get_json()
    assert "hostname" in data
    assert "python_version" in data
    assert "environment" in data
    assert "timestamp" in data


def test_index_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_page_contains_dashboard_title(client):
    response = client.get("/")
    assert b"DevOps Health Dashboard" in response.data
