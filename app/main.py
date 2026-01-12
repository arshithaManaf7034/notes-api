from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import traceback

from app.db.init_db import init_db
from app.api import auth, notes, versions

app = FastAPI(title="Notes API with Version History")

# GLOBAL EXCEPTION HANDLER (DEBUGGING)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),
            "traceback": traceback.format_exc(),
        },
    )

# CREATE TABLES ON STARTUP
init_db()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://notes-frontend-.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(versions.router, tags=["Versions"])

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/debug")
def debug():
    return {"debug": "ok"}
