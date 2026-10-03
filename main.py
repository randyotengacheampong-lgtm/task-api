from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="TaskFlow API", version="1.0")

# Allow frontend to talk to backend (VERY IMPORTANT for Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Task model
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = ""
    completed: bool = False

# In-memory database
tasks: List[Task] = []
task_id_counter = 1

@app.get("/api")
def root():
    return {"message": "TaskFlow API is running! Go to /docs for API docs"}

@app.get("/api/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/api/tasks", response_model=Task)
def create_task(task: Task):
    global task_id_counter
    task.id = task_id_counter
    task_id_counter += 1
    tasks.append(task)
    return task

@app.put("/api/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            updated_task.id = task_id
            tasks[i] = updated_task
            return updated_task
    return {"detail": "Task not found"}

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id!= task_id]
    return {"message": "Task deleted"}

# --- SERVE FRONTEND (This fixes your "Not Found" error) ---
if os.path.exists("index.html"):
    @app.get("/")
    async def serve_frontend():
        return FileResponse("index.html")
    