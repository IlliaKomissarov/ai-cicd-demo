# tests/conftest.py
import pytest
from src.app import app as flask_app

@pytest.fixture
def app():
    yield flask_app