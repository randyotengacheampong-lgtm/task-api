from fastapi import FastAPI, HTTPException
from database import get_db_connection, init_db
from models import TaskCreate, TaskUpdate, Task
from typing import List

app = FastAPI()
init_db()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    if len(task.title.strip()) < 3:
        raise HTTPException(status_code=400, detail="Title must be at least 3 characters")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, completed) VALUES (?,?,?)",(task.title, task.description, False))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task.title, "description": task.description, "completed": False}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [dict(row) for row in tasks]

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM tasks WHERE id =?", (task_id,)).fetchone()
    conn.close()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(task)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    conn = get_db_connection()
    existing = conn.execute("SELECT * FROM tasks WHERE id =?", (task_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.execute("UPDATE tasks SET title=?, description=?, completed=? WHERE id=?", (task.title, task.description, False, task_id))
    conn.commit()
    updated = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    conn.close()
    return dict(updated)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    existing = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted"}
