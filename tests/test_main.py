from fastapi.testclient import TestClient
from main import app
from database import SessionLocal, Base, engine
import pytest

# Create a new test client
client = TestClient(app)

# Set up a test database
@pytest.fixture(scope="function")
def setup_database():
    """Creates a fresh test database before each test"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_validate_despatch_success(setup_database):
    """Test successful validation"""
    data = {
        "key1": "delivery",
        "key2": "Valid note",
        "key3": "Item1",
        "key4": "Item description"
    }
    response = client.post("/validate_despatch/", json=data)
    assert response.status_code == 200
    assert response.json()["statusCode"] == 200
    assert response.json()["body"]["DespatchAdviceTypeCode"] == "delivery"

def test_validate_despatch_invalid_code(setup_database):
    """Test invalid despatch advice type"""
    data = {
        "key1": "invalid_code",
        "key2": "Valid note",
        "key3": "Item1",
        "key4": "Item description"
    }
    response = client.post("/validate_despatch/", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "DespatchAdviceTypeCode is not valid, please update"

def test_validate_despatch_long_note(setup_database):
    """Test note length validation"""
    data = {
        "key1": "delivery",
        "key2": "This note is way too long and should not be accepted.",
        "key3": "Item1",
        "key4": "Item description"
    }
    response = client.post("/validate_despatch/", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Note is too long, please update"

