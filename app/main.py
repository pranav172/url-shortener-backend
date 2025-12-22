from fastapi import FastAPI

app = FastAPI(title="URL Shortener")

@app.get("/")
def health():
    return {"status": "ok"}
