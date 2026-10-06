# TaskFlow ⚡ — Fullstack Task Manager
Small but powerful Task API built to learn FastAPI — built in Accra, Ghana 🇬🇭

[![Live](https://img.shields.io/badge/Live-Production-success)](https://task-api-phi-weld.vercel.app/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Deployed](https://img.shields.io/badge/Deployed-Vercel%20%2B%20Render-black)](https://vercel.com)

### 🚀 Live Links
- **Frontend (Live App):** https://task-api-phi-weld.vercel.app/
- **Backend (Live API):** https://task-api-ze8n.onrender.com
- **API Docs (Swagger):** https://task-api-ze8n.onrender.com/docs
- **GitHub:** https://github.com/randyotengacheampong-lgtm/task-api

### ✨ Features
- Create, Read, Update, Delete Tasks (Full CRUD)
- Interactive Swagger Docs at `/docs`
- FastAPI backend with auto-validation
- Clean Vanilla JS Frontend
- Deployed fullstack: Vercel + Render

### 📚 API Endpoints
From live Swagger at `/docs`:

- `GET /api` - Root
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task
- `GET /` - Serve Frontend UI

### 🛠️ Tech Stack
**Backend:** Python, FastAPI, Uvicorn, SQLite, SQLAlchemy/Pydantic
**Frontend:** HTML, CSS, Vanilla JavaScript
**Deployment:** Render (API) + Vercel (Frontend)

### 💻 Run Locally
```bash
# Clone
git clone https://github.com/randyotengacheampong-lgtm/task-api.git
cd task-api

# Install
pip install -r requirements.txt

# Run
uvicorn main:app --reload

# Open http://127.0.0.1:8000/docs for API docs

👨‍💻 Author
Randy Oteng Acheampong (Kofi) — Software Developer, Accra, Ghana 🇬🇭
 •  GitHub: @randyotengacheampong-lgtm
 •  Stack: FastAPI & JavaScript
 •  Mission: Building real products, not just tutorials
 