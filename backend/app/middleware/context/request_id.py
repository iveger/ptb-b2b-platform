import re
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

REQUEST_ID_HEADER = "X-Request-ID"

# Разрешаем безопасный формат (чтобы не пихали мусор/инъекции в логи)
_REQUEST_ID_RE = re.compile(r"^[a-zA-Z0-9_\-:.]{8,128}$")


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        incoming = request.headers.get(REQUEST_ID_HEADER)

        if incoming and _REQUEST_ID_RE.match(incoming):
            request_id = incoming
        else:
            request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = await call_next(request)
        response.headers[REQUEST_ID_HEADER] = request_id
        return response
