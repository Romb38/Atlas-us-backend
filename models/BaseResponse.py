class BaseResponse:
    """
    HTTP Base Request
    :ivar code: Response code
    :ivar message: Response message
    """
    code: int
    message: str

    def __init__(self, code, message):
        self.code = code
        self.message = message

    @staticmethod
    def success():
        return BaseResponse(0, "Success")
