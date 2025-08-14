from datetime import datetime, timedelta
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.auth_schemas import Token
from app.utils.password_hashing import hash_password, verify_password
from app.CRUD import user_crud
from sqlalchemy.orm import Session
from app.utils.token_handler import encode_token, decode_token
from app.database import get_db

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def authenticate_user(db: Session, username: str, password: str):
    user = user_crud.get_user(db, username = username)
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

@auth_router.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = encode_token({
        "username": user.username,
        "email": user.email,
        "rol": user.role,
        "expiration": str(datetime.utcnow() + timedelta(minutes=30))
    })
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="access_token",  # Cookie Name
        value=f"Bearer {token}",
        httponly=True,  # Access only by the server
        samesite="Strict"
    )
    return response

@auth_router.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie("access_token")
    return response