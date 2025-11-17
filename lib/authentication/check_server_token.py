from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

server_token_header = APIKeyHeader(name=config("SERVER_TOKEN_HEADER", default="Server-Token"), auto_error=True)


def verify_server_token(token: str = Depends(server_token_header)):
    """
    Check server token
    :param token: Current token fetched from SERVER_TOKEN_HEADER
    :return: True if the token is valid
    :exception 401: if the token is invalid
    :exception 403: if the header is missing
    """
    server_token = config("SERVER_TOKEN", default="")
    if server_token and token != server_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid server token",
        )
    return True
