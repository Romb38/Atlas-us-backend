from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from lib.authentication import get_current_user
from lib.database import engine
from models import User, BaseResponse
from .model import LoginRequest, UpdatePasswordRequest
from .service import verify_password, create_access_token, get_password_hash

router = APIRouter()

@router.post(
    "/login",
    description="Log a user in the system and return a JWT token",
    response_model=str,
    response_description="Authorization JWT token",
)
async def login(request: LoginRequest):
    """
    Log a user in the system and return a JWT token
    :param request: Login information
    :return: A JWT token for the user
    """
    with Session(engine) as session:
        statement = select(User).where(User.username == request.username)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=400, detail="Nom d'utilisateur incorrect")

        if not verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=400, detail="Mot de passe incorrect")

        return create_access_token(user.username)


@router.post(
    "/register",
    description="Register a new user",
    response_model=str,
    response_description="Authorization JWT token",
)
async def register(request: LoginRequest):
    """
    Register a new user
    :param request: Register information
    :return: A JWT token for the new user
    """
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

        return create_access_token(new_user.username)

@router.post(
    "/update-password",
    description="Update a user's password",
    response_model=BaseResponse,
    response_description="Authorization JWT token",
)
def update_password(
    request: UpdatePasswordRequest,
    current_user: User = Depends(get_current_user),
):
    """
    Update a user's password
    :param request: Updated password request
    :param current_user: `(autofilled)` Current logged user
    :return: Basic success response
    """
    hashed_password = get_password_hash(request.new_password)

    with Session(engine) as session:
        db_user = session.get(User, current_user.id)
        db_user.password_hash = hashed_password
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return BaseResponse.success()