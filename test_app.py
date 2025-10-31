from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

# ✅ Create a test client
client = TestClient(app)

def test_get_fruits_empty():
    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": []}

def test_add_fruit():
    response = client.post("/fruits", json={"name": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"name": "Apple"}

    # Check that GET now returns the added fruit
    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": [{"name": "Apple"}]}
    

    
