# TaskFlow ⚡ — task-api
Small API I am building to learn FastAPI — built in Accra, Ghana 🇬🇭

Just went LIVE full-stack! 🚀

## 🚀 Live Links
- **Frontend (Vercel):** https://task-api-phi-weld.vercel.app/
- **Backend (Render):** https://task-api-ze8n.onrender.com
- **API Docs:** https://task-api-ze8n.onrender.com/docs
- **GitHub:** https://github.com/randyotengacheampong-lgtm/task-api

## ✨ What I Built Tonight
- Deployed FastAPI backend to Render
- Deployed Vanilla JS frontend to Vercel
- Fixed CORS + frontend not found issue
- Connected frontend to live API (`/api/tasks`)
- Full CRUD now works LIVE on the internet!

## 📚 API - Currently complete CRUD with SQLite
- POST /api/tasks - Create a task
- GET /api/tasks - List all tasks
- GET /tasks/{id} - Get one task
- PUT /api/tasks/{id} - Update a task
- DELETE /api/tasks/{id} - Delete a task

## 🛠️ Stack
Python, FastAPI, Uvicorn, SQLite, Vanilla JS, Vercel, Render

## How to run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload