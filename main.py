from fastapi import FastAPI, Depends
from sqlmodel import SQLModel

from lib.authentication.check_auth import get_current_user
from lib.authentication.check_server_token import verify_server_token
from lib.database.database import engine
from routes.auth import auth_router

SQLModel.metadata.create_all(engine)
app = FastAPI(dependencies=[Depends(verify_server_token)])

@app.get("/ping")
def ping():
    return "pong"

@app.get("/sping")
def sping(
    user = Depends(get_current_user)
):
    return "pong : " + user.username


app.include_router(auth_router)