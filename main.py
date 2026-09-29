from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Task as DBTask

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "task api running with database!"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(DBTask).all()
    return tasks

@app.post("/tasks")
def add_task(title: str, db: Session = Depends(get_db)):
    new_task = DBTask(title=title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task