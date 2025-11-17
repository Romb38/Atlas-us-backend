from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from lib.database.database import engine
from models.User import User
from routes.auth.model.LoginRequest import LoginRequest
from routes.auth.service.login_service import create_access_token, verify_password, get_password_hash

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest):
    with Session(engine) as session:
        statement = select(User).where(User.username == request.username)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=400, detail="Nom d'utilisateur incorrect")

        if not verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=400, detail="Mot de passe incorrect")

        return create_access_token({"sub": user.username})


@router.post("/register")
async def register(request: LoginRequest):
    with Session(engine) as session:
        statement = select(User).where(User.username == request.username)
        existing_user = session.exec(statement).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_password = get_password_hash(request.password)

        new_user = User(username=request.username, password_hash=hashed_password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return create_access_token({"sub": new_user.username})
