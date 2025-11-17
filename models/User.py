from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """
    Represents a user in the system
    :ivar id: Unique identifier of the user
    :ivar username: Username of the user
    :ivar password_hash: Password of the user (hashed)
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str
