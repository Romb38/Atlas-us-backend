from pydantic import BaseModel


class LoginRequest(BaseModel):
    """
    Represent a login request or a register request
    :ivar str username: Username for login or register
    :ivar str password: Password for login or register (plain)
    """

    username: str
    password: str
