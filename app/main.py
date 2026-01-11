from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, notes, versions
from app.db.session import engine
from app.db.base import Base   # 👈 IMPORTANT

# ✅ CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API with Version History")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://notes-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(versions.router, tags=["Versions"])

@app.get("/")
def health():
    return {"status": "ok"}
