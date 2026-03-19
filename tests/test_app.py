import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"
def test_list_items():
    res = client.get("/items/")
    assert res.status_code == 200
def test_create_item():
    res = client.post("/items/", json={"name": "widget"})
    assert res.status_code == 200
    assert res.json()["name"] == "widget"
