import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from loguru import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.perf_counter()

        # request_id, если middleware уже отработал
        request_id = getattr(request.state, "request_id", "-")

        try:
            response = await call_next(request)
        except Exception:
            duration_ms = (time.perf_counter() - start) * 1000
            logger.exception(
                f"[REQ] id={request_id} "
                f"{request.method} {request.url.path} -> 500 "
                f"({duration_ms:.1f}ms)"
            )
            raise

        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            f"[REQ] id={request_id} "
            f"{request.method} {request.url.path} -> {response.status_code} "
            f"({duration_ms:.1f}ms)"
        )
        return response
