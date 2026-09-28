from fastapi import FastAPI

app = FastAPI()

# just storing in memory for now, will use db later
tasks = []

@app.get("/")
def home():
    return {"message": "task api running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(title: str):
    # quick add, need validation later
    new_task = {"id": len(tasks) + 1, "title": title}
    tasks.append(new_task)
    return new_task
