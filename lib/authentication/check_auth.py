import jwt
from decouple import config
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session, select
from starlette import status

from lib.database.database import engine
from models.User import User

security = HTTPBearer()


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    """
    Fetch user information and return it
    :param credentials: `(autofilled)` User bearer token (fetched from Authorization header)
    :return: Current user data
    :exception 401: Unauthorized if username isn't set, token is invalid or user isn't found
    :exception 403: Forbidden if token is expired
    """
    token = credentials.credentials
    secret_key = config("SECRET_KEY", default="YOU_SHOULD_NOT_BE_HERE")
    algorithm = config("HASH_ALGORITHM", default="HS256")
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired token",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid user",
            )

    return user
