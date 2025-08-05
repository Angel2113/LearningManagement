from typing import Annotated

from dns.dnssectypes import Algorithm
from fastapi import FastAPI, Depends
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="get_token")

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    return token

def decode_token(token:str ) -> dict:
    data = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    return data