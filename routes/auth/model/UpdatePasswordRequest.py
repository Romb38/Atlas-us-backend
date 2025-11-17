from pydantic import BaseModel


class UpdatePasswordRequest(BaseModel):
    """
    Class for updating password
    :ivar str new_password: Updated password (plain)
    """

    new_password: str
