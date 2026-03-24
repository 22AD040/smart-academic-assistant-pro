from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running"}

# 🔥 ADD THIS
@app.head("/")
def head_root():
    return {"status": "ok"}