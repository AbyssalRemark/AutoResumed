from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
import pytest
from app import create_app

@pytest.fixture(autouse=True, scope="session")
def app():
    app = create_app()
    app.config.update({"TESTING": True})

    yield app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_auth_register(client: FlaskClient):
    response = client.post("/auth/register", json={
        "email" : "testy_mctest@example.com",
        "password": "insecure_password_123",
    })

    assert response.json["message"] == "Registration successful." # pyright: ignore

def test_auth_login(client: FlaskClient):
    response = client.get("/auth/login")

def test_auth_logout(client: FlaskClient):
    response = client.get("/auth/logout")
