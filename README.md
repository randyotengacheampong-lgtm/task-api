# task-api
Small API I am building to learn FastAPI — built in Accra, Ghana 🇬🇭

Currently complete CRUD with SQLite:
- POST /tasks - Create a task
- GET /tasks - List all tasks
- GET /tasks/{id} - Get one task
- PUT /tasks/{id} - Update a task
- DELETE /tasks/{id} - Delete a task

## How to run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
🚀 Live: https://task-api-ze8n.onrender.com
📚 Docs: https://task-api-ze8n.onrender.com/docs
💻 Frontend: index.html — TaskFlow UI (open index.html to use it)