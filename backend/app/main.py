from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import transaksi
from app.core.config import get_settings

app = FastAPI(
    title="CatatAI API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaksi.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "ok", "app": "CatatAI"}

@app.get("/health")
def health():
    s = get_settings()
    return {
        "status": "sehat",
        "groq_api_key": bool(s.groq_api_key),
        "supabase_url": bool(s.supabase_url),
    }
