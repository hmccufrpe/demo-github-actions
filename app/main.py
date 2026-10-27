from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks API")

_tasks: dict[int, dict] = {}
_next_id = 1


class TaskIn(BaseModel):
    title: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", status_code=201)
def create_task(body: TaskIn):
    global _next_id
    task = {"id": _next_id, "title": body.title, "done": False}
    _tasks[_next_id] = task
    _next_id += 1
    return task


@app.get("/tasks")
def list_tasks():
    return list(_tasks.values())


@app.patch("/tasks/{task_id}/done")
def complete_task(task_id: int):
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task["done"] = False
    return task
