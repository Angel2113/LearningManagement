from fastapi import FastAPI
from app.routes.users_router import users_router
from app.routes.auth_router import auth_router
from fastapi.security import OAuth2PasswordBearer
from app.CRUD.user_crud import CRUDUser
from app.utils.token_handler import encode_token

app = FastAPI(
    title="Learning Management",
    description="Learning Management API Backend",
    version="0.0.1"
)
oauth_scheme = OAuth2PasswordBearer(tokenUrl="get_token")

app.include_router(users_router)
app.include_router(auth_router)

app.title = "Learning Management"
app.version = "0.0.1"
@app.get("/", tags=["Home"])
async def get_home():
    return {"message": "Hello World"}