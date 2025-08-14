from typing import Annotated

from dns.dnssectypes import Algorithm
from fastapi import FastAPI, Depends
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Request, HTTPException
import jwt
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="get_token")

def encode_token(payload: dict) -> str:
    print(f"JWT_SECRET: {JWT_SECRET}")
    print(f"ALGORITH: {ALGORITHM}")
    logger.info(f"JWT_SECRET: {JWT_SECRET}")
    logger.info(f"ALGORITH: {ALGORITHM}")
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    return token

def decode_token(request:Request ) -> dict:
    ## Preview version data = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    ## return data
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="No access token")
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return data



