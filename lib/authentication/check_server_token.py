from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from decouple import config

server_token_header = APIKeyHeader(name=config("SERVER_TOKEN_HEADER", default="Server-Token"), auto_error=True)

def verify_server_token(token: str = Depends(server_token_header)):
    server_token = config("SERVER_TOKEN",default="")
    if token != server_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid server token",
        )
    return True