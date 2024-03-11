from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
import pytest
from app import create_app

@pytest.fixture(autouse=True, scope="session")
def app_dict():
    app = create_app()
    app.config.update({"TESTING": True})

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()

@pytest.fixture()
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()

def test_auth_register(client: FlaskClient):
    response = client.get("/auth/register")

def test_auth_login(client: FlaskClient):
    response = client.get("/auth/login")

def test_auth_logout(client: FlaskClient):
    response = client.get("/auth/logout")
