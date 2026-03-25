from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()


app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running"}

@app.head("/")
def head_root():
    return {"status": "ok"}