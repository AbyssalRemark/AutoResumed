from flask import Flask
from flask.testing import FlaskClient
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


def test_auth(client: FlaskClient):
    credentials = {
        "email" : "testy_mctest@example.com",
        "password": "insecure_password_123",
    }

    register_response = client.post("/auth/register", json=credentials)
    assert register_response.json["message"] == "Registration successful." # pyright: ignore

    login_response = client.post("/auth/login", json=credentials)
    token = login_response.json["token"] # type: ignore
    assert len(token) != 0

    delete_reponse = client.post("auth/delete", json={
        "token": token
    })
    assert delete_reponse.json["message"] == "Deletion sucessful." # type: ignore
