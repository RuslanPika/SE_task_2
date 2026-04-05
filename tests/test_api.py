from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working"}

def test_generate():
    response = client.post("/generate", json={"prompt": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "Hello" in data["response"]