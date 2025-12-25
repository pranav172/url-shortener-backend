# 🔗 Scalable URL Shortener (FastAPI + PostgreSQL + Redis)

A production-ready URL Shortener backend built with FastAPI, designed with scalability, performance, and reliability in mind.

## 🌐 Live Links
- **Live API:** https://url-shortener-backend-fgyj.onrender.com
- **API Docs (Swagger):** https://url-shortener-backend-fgyj.onrender.com/docs

## 🚀 Features
- 🔗 URL shortening using Base62 encoding
- ⚡ Fast redirects with Redis caching
- ⏳ Link expiry support (time-based)
- 🛡️ Rate limiting to prevent abuse
- 🧠 Graceful degradation (Redis / DB failure handling)

## 🏗️ Architecture
Client → FastAPI → Redis → PostgreSQL



## 🧪 API Endpoints

### Health Check
GET /


### Create Short URL
POST /shorten



**Request:**
```json
{
  "original_url": "https://www.google.com"
}
Response:

json
{
  "short_url": "https://url-shortener-backend-fgyj.onrender.com/abc123"
}
Redirect
GET /{short_code}
⚙️ Tech Stack
Backend: FastAPI, Python

Database: PostgreSQL

Cache: Redis

ORM: SQLAlchemy

Deployment: Render

🛠️ Local Setup
pip install -r requirements.txt
uvicorn app.main:app --reload

👤 Author
Pranav Raj
GitHub: https://github.com/pranav172
LinkedIn: https://linkedin.com/in/pranav-raj-163230256
