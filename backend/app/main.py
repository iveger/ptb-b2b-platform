from fastapi import FastAPI

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="0.1.0",
    )

    @app.get("/health", tags=["system"])
    async def health_check():
        return {"status": "ok"}

    return app


app = create_app()

