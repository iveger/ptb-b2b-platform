from fastapi import FastAPI
from app.core.config import settings
from app.core.lifecycle import on_startup, on_shutdown
from app.api.v1.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    @app.get("/health", tags=["health"])
    def root_health():
        return {"status": "ok"}

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app


app = create_app()
