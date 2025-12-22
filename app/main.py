from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal, Base
from app import models
from app.models import URL
from app.schemas import URLCreate, URLResponse
from app.utils import encode_base62

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

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
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
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
