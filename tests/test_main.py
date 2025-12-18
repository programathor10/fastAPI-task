from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root_should_return_ok_and_message():
    # 1. Hacer un GET a "/"
    response = client.get("/")
    # 2. Verificar que el status code sea 200
    assert response.status_code == 200
    # 3. Verificar que el JSON devuelto sea el esperado
    assert response.json() == {"message": "API de Tasks funcionando"}

def test_post():
    data = {"name": "Tarea test", "description": "Descripción test"}
    response = client.post("/tasks/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Tarea test"
    assert response.json()["description"] == "Descripción test"
    assert "id" in response.json()

def test_get():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert type(response.json()) is list
    assert len(response.json()) >= 1

def test_task_id():
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_dummy():
    assert 1 == 1
