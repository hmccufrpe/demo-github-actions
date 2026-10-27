import pytest
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_state():
    main._tasks.clear()
    main._next_id = 1


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_list_task():
    r = client.post("/tasks", json={"title": "Estudar Actions"})
    assert r.status_code == 201
    assert r.json()["done"] is False
    assert len(client.get("/tasks").json()) == 1


def test_complete_task():
    client.post("/tasks", json={"title": "Fazer demo"})
    r = client.patch("/tasks/1/done")
    assert r.status_code == 200
    assert r.json()["done"] is True


def test_complete_missing_task_returns_404():
    assert client.patch("/tasks/99/done").status_code == 404
