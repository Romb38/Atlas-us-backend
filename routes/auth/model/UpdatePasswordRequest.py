from pydantic import BaseModel

class UpdatePasswordRequest(BaseModel):
    new_password: str