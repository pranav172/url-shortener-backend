# 🔗 Scalable URL Shortener (FastAPI + PostgreSQL + Redis)

A production-ready URL Shortener backend built with FastAPI, designed with scalability, performance, and reliability in mind.  
The system supports URL shortening, fast redirects using Redis caching, rate limiting, link expiry, and is deployed live on Render.

🌐 **Live API:**  
https://url-shortener-backend-fgyj.onrender.com  

📘 **API Docs (Swagger):**  
https://url-shortener-backend-fgyj.onrender.com/docs  

---

## 🚀 Features

- 🔗 URL shortening using Base62 encoding
- ⚡ Fast redirects with Redis caching (cache-aside pattern)
- ⏳ Link expiry support (time-based)
- 🛡️ Rate limiting to prevent abuse
- 🧠 Graceful degradation (Redis / DB failure handling)
- 🌍 Deployed on Render with managed PostgreSQL & Redis
- 🔐 Secure configuration via environment variables

---

## 🏗️ Architecture Overview

Client
↓
FastAPI (Uvicorn)
↓
Redis (cache, rate limiting)
↓
PostgreSQL (persistent storage)

yaml
Copy code

- Redirects first hit Redis for low-latency responses
- Database is accessed only on cache miss
- Expired links return HTTP 410
- Rate limiting is applied per client IP

---

## 🧪 API Endpoints

### Health Check
GET /

clean
Copy code

### Create Short URL
POST /shorten

autohotkey
Copy code

**Request**
```json
{
  "original_url": "https://www.google.com"
}
Response

json
Copy code
{
  "short_url": "https://url-shortener-backend-fgyj.onrender.com/abc123"
}
Redirect
routeros
Copy code
GET /{short_code}
⚙️ Tech Stack
Backend: FastAPI, Python

Database: PostgreSQL

Cache: Redis

ORM: SQLAlchemy

Deployment: Render

API Docs: Swagger (OpenAPI)

📈 Scaling Considerations
Redis caching reduces database load for high read traffic

Indexed lookups on short_code ensure fast queries at scale

Expired links are validated at request time

Architecture supports horizontal scaling behind a load balancer

🛠️ Local Setup (Optional)
bash
Copy code
pip install -r requirements.txt
uvicorn app.main:app --reload
👤 Author
Pranav Raj
GitHub: https://github.com/pranav172
LinkedIn: https://linkedin.com/in/pranav-raj-163230256
