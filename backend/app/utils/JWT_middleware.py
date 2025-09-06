from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, HTTPException, FastAPI, Response, status
from app.utils.token_handler import decode_token
from starlette.responses import JSONResponse
from datetime import datetime
import logging

EXCLUDE_PATHS = ["/home", "/auth/login", "/docs", "/openapi.json", "/register"]

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class JWTMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        auth_header = request.headers.get("Authorization")
        logger.info(f"PATH: {request.url.path}")
        # Exclude paths from authentication
        if request.url.path in EXCLUDE_PATHS:
            return await call_next(request)

        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Unauthorized - Missing token"})

        token = auth_header.split("Bearer ")[1]
        logger.info(f"Token: {token}")
        try:
            payload = decode_token(token)
            logger.info(f"Payload: {payload}")
            request.state.user = payload["username"]
            request.state.user_id = payload["user_id"]
            request.state.role = payload["role"]
            exp_date = payload["expiration"]
            current_time = datetime.now().isoformat()

            if current_time > exp_date:
                return JSONResponse(content="Unauthorized - Token expired", status_code=status.HTTP_401_UNAUTHORIZED)

            logger.info(f"Payload: {payload}")
        except Exception as e:
            return JSONResponse(content="Unauthorized - Invalid token", status_code=status.HTTP_401_UNAUTHORIZED)

        return await call_next(request)