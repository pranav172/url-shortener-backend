from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import URL
from app.schemas import URLCreate, URLResponse
from app.utils import encode_base62

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLResponse)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    url = URL(original_url=payload.original_url)
    db.add(url)
    db.commit()
    db.refresh(url)

    short_code = encode_base62(url.id)
    url.short_code = short_code
    db.commit()

    return {"short_url": f"http://localhost:8000/{short_code}"}
