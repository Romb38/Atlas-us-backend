from fastapi import Depends, FastAPI
from sqlmodel import SQLModel

from lib.authentication.check_auth import get_current_user
from lib.authentication.check_server_token import verify_server_token
from lib.database.database import engine
from routes.auth import auth_router

SQLModel.metadata.create_all(engine)
app = FastAPI(
    docs_url=None,  # Deactivate Swagger UI
    redoc_url=None,  # Deactivate Redoc
    openapi_url=None,  # Deactivate OpenAPI schema
    dependencies=[Depends(verify_server_token)],
)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/sping")
def sping(user=Depends(get_current_user)):
    return "pong : " + user.username


app.include_router(auth_router)
