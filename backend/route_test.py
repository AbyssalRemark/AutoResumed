import pytest
from app import create_app

@pytest.fixture(autouse=True, scope="session")
def app_dict():
    app = create_app()
    app.config.update({"TESTING": True})
