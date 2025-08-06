from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, HTTPException, FastAPI, Response, status
from app.utils.token_handler import decode_token
from starlette.responses import JSONResponse


class JWTMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Unauthorized - Missing token"})

        token = auth_header.split("Bearer ")[1]
        try:
            payload = decode_token(token)
            request.state.user = payload["username"]
        except Exception as e:
            return JSONResponse(content="Unauthorized - Invalid token", status_code=status.HTTP_401_UNAUTHORIZED)

        return await call_next(request)