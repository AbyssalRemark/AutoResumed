from flask import Flask
import pytest
from app import create_app

@pytest.fixture(autouse=True, scope="session")
def app_dict():
    app = create_app()
    app.config.update({"TESTING": True})

@pytest.fixture()
def client(app: Flask):
    return app.test_client()

@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()
