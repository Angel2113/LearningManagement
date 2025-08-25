from datetime import datetime, timedelta
from typing import Annotated
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth_schemas import Token, UserRequest
from app.utils.password_hashing import hash_password, verify_password
from app.CRUD import user_crud
from sqlalchemy.orm import Session
from app.utils.token_handler import encode_token, decode_token
from app.database import get_db
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

#oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
security = HTTPBearer()

def authenticate_user(db: Session, username: str, password: str):
    user = user_crud.get_user(db, username = username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

def get_current_user(token: Annotated[str, Depends(security)]):
    try:
        payload = decode_token(token)
        username: str = payload.get("username")
        user_id: str = payload.get("user_id")
        role: str = payload.get("role")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {
            "username": username,
            "user_id": user_id,
            "role": role,
        }
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@auth_router.post("/login", response_model=Token)
async def login(user: UserRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = encode_token({
        "user_id": str(user.id),
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "expiration": (datetime.now() + timedelta(minutes=30)).isoformat()
    })
    return { "access_token": token, "token_type": "bearer" }

@auth_router.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie("access_token")
    return response