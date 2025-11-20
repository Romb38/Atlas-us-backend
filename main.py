from fastapi import Depends, FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from lib.authentication import get_current_user, verify_server_token
from lib.database import engine
from routes.auth import router as auth_router

SQLModel.metadata.create_all(engine)
app = FastAPI(
    docs_url=None,  # Deactivate Swagger UI
    redoc_url=None,  # Deactivate Redoc
    openapi_url=None,  # Deactivate OpenAPI schema
    dependencies=[Depends(verify_server_token)],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/sping")
def sping(user=Depends(get_current_user)):
    return "pong : " + user.username


app.include_router(auth_router)
