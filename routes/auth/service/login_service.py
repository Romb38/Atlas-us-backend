import datetime

import jwt
from decouple import config
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies password against hashed password

    :param plain_password: Password to be verified
    :param hashed_password: Hashed password to compare with
    :return: True if password matches hashed password, else False
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Gets password hash
    :param password: Plain password to hash
    :return: Hashed password
    """
    return pwd_context.hash(password)


def create_access_token(username: str) -> str:
    """
    Creates a JWT token from
    :param username: Username of the user to login
    :return: A JWT token
    """
    expiration_time = int(config("ACCESS_TOKEN_EXPIRE_MINUTES", default=60))
    secret_key = config("SECRET_KEY", default="YOU_SHOULD_NOT_BE_HERE")
    algorithm = config("HASH_ALGORITHM", default="HS256")
    now = datetime.datetime.now(datetime.UTC)

    expire = now + datetime.timedelta(minutes=expiration_time)

    to_encode = {
        "sub": username,
        "iat": now,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt
