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

## 📚 API Endpoints (from live docs)
As shown in Swagger at `/docs`:

- `GET /api` - Root
- `GET /api/tasks` - Get Tasks (list all)
- `POST /api/tasks` - Create Task
- `PUT /api/tasks/{task_id}` - Update Task
- `DELETE /api/tasks/{task_id}` - Delete Task
- `GET /` - Serve Frontend (TaskFlow UI)

## 🛠️ Stack
Python, FastAPI, Uvicorn, SQLite, Vanilla JS, Vercel, Render

## How to run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
## 👨‍💻 Author
**Randy Oteng Acheampong (Kofi)** — Software Developer, Accra, Ghana 🇬🇭
- GitHub: [@randyotengacheampong-lgtm](https://github.com/randyotengacheampong-lgtm)
- Building with FastAPI & JavaScript