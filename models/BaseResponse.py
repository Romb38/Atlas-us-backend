from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    HTTP Base Request
    :ivar code: Response code
    :ivar message: Response message
    """

    code: int
    message: str

    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.message = message

    @staticmethod
    def success():
        return BaseResponse(0, "Success")
