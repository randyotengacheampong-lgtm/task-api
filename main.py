from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# THIS FIXES THE CONNECTION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB setup
conn = sqlite3.connect("tasks.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, description TEXT, completed BOOLEAN DEFAULT 0)")

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskUpdate(BaseModel):
    title: str = None
    completed: bool = None

@app.get("/tasks")
def get_tasks():
    cur = conn.execute("SELECT id, title, description, completed FROM tasks")
    rows = cur.fetchall()
    return [{"id": r[0], "title": r[1], "description": r[2], "completed": bool(r[3])} for r in rows]

@app.post("/tasks")
def create_task(task: TaskCreate):
    cur = conn.execute("INSERT INTO tasks (title, description, completed) VALUES (?,?, 0)", (task.title, task.description))
    conn.commit()
    return {"id": cur.lastrowid, "title": task.title, "description": task.description, "completed": False}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    if task.title is not None:
        conn.execute("UPDATE tasks SET title=? WHERE id=?", (task.title, task_id))
    if task.completed is not None:
        conn.execute("UPDATE tasks SET completed=? WHERE id=?", (int(task.completed), task_id))
    conn.commit()
    return {"status": "updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    return {"status": "deleted"}
