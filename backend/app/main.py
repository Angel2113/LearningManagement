from typing import Annotated

from fastapi import FastAPI, requests, Response, Header, Depends, HTTPException, Cookie
from app.routes.users_router import users_router
from app.routes.auth_router import auth_router
from app.routes.goals_router import goals_router
from app.routes.chat_router import chat_router
from fastapi.security import OAuth2PasswordBearer
from app.CRUD import user_crud
from app.utils.token_handler import encode_token
from app.utils.JWT_middleware import JWTMiddleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Learning Management",
    description="Learning Management API Backend",
    version="0.0.2"
)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(goals_router)
app.include_router(chat_router)

#oauth_scheme = OAuth2PasswordBearer(tokenUrl="get_token")
app.add_middleware(JWTMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_headers(
        access_token: Annotated[str | None, Header()] = None,
        user_role: Annotated[list[str] | None, Header()] = None
):
    if access_token != "secret-token":
            raise HTTPException(status_code=401, detail="Unauthorized")
    return {"MyHeader": "Hola"}

@app.get("/", tags=["Home"])
async def get_home(headers: Annotated[dict, Depends(get_headers)]):
    return {"access_token": headers['access_token'], "user_role": headers['user_role']}

