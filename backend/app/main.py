from fastapi import FastAPI, Depends
from app.routes.users_router import users_router
app = FastAPI()

app.include_router(users_router)

app.title = "Learning Management"
app.version = "0.0.1"
@app.get("/", tags=["Home"])
async def get_home():
    return {"message": "Hello World"}
