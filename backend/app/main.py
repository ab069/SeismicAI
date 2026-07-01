from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import init_db
from app.api import auth, surveys, horizons, prospects, ws


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="SeismicAI", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(surveys.router)
app.include_router(horizons.router)
app.include_router(prospects.router)
app.include_router(ws.router)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "SeismicAI"}
