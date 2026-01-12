from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="ptb-b2b-platform",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(health_router)
