
import time
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from collections import defaultdict
from fastapi import Request
from app.database import engine, SessionLocal, Base
from app import models
from app.models import URL
from app.schemas import URLCreate, URLResponse
from app.utils import encode_base62

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

RATE_LIMIT = 5        # max requests
WINDOW_SIZE = 60      # seconds

request_log = defaultdict(list)

def check_rate_limit(ip: str):
    current_time = time.time()
    window_start = current_time - WINDOW_SIZE

    # Remove old timestamps
    request_log[ip] = [
        t for t in request_log[ip] if t > window_start
    ]

    if len(request_log[ip]) >= RATE_LIMIT:
        return False

    request_log[ip].append(current_time)
    return True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health check
@app.get("/")
def health():
    return {"status": "ok"}

# Create short URL
@app.post("/shorten", response_model=URLResponse)
def shorten_url(
    payload: URLCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    client_ip = request.client.host

    if not check_rate_limit(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )

    url = URL(original_url=str(payload.original_url))
    db.add(url)
    db.commit()
    db.refresh(url)

    short_code = encode_base62(url.id)
    url.short_code = short_code
    db.commit()

    return {"short_url": f"http://localhost:8000/{short_code}"}

# Redirect endpoint (YOU ADD THIS)
@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.original_url)
