from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users_db = {}
tasks_db = {}
task_id_counter = 1

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/register")
def register(data: dict):
    username = data.get("username")
    password = data.get("password")
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[username] = get_password_hash(password)
    return {"message": "User created"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    hashed = users_db.get(username)
    if not hashed:
        raise HTTPException(status_code=401, detail="User not found")
    if not verify_password(password, hashed):
        raise HTTPException(status_code=401, detail="Wrong password")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/tasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    return {"user": current_user, "tasks": tasks_db.get(current_user, [])}

@app.post("/tasks")
def create_task(data: dict, current_user: str = Depends(get_current_user)):
    global task_id_counter
    task = {"id": task_id_counter, "title": data.get("title"), "completed": False}
    task_id_counter += 1
    if current_user not in tasks_db:
        tasks_db[current_user] = []
    tasks_db[current_user].append(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    user_tasks = tasks_db.get(current_user, [])
    for i, t in enumerate(user_tasks):
        if t.get("id") == task_id:
            user_tasks.pop(i)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
