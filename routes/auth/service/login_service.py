import datetime

import jwt
from decouple import config
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict):
    expiration_time = int(config("ACCESS_TOKEN_EXPIRE_MINUTES", default=60))
    secret_key = config("SECRET_KEY", default="YOU_SHOULD_NOT_BE_HERE")
    algorithm = config("HASH_ALGORITHM", default="HS256")
    now = datetime.datetime.now(datetime.UTC)

    to_encode = data.copy()
    expire = now + datetime.timedelta(minutes=expiration_time)

    to_encode.update({
        "iat": now,
        "exp": expire,
    })

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

