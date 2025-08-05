from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.auth_schemas import Token
from app.utils.password_hashing import hash_password, verify_password
from app.CRUD.user_crud import CRUDUser
from app.utils.token_handler import encode_token, decode_token

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def authenticate_user(username: str, password: str):
    user = CRUDUser().get_user(username = username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = decode_token(token)
        username: str = payload.get("username")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {'username': username}
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@auth_router.post("/get_token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = encode_token({
        "username": user.username,
        "email": user.email,
        "rol": user.role,
        "expiration": str(datetime.utcnow() + timedelta(minutes=30))
    })
    return { "access_token": token, "token_type": "bearer" }
