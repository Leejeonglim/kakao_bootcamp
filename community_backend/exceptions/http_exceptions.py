# 2-3 exception

from fastapi import HTTPException

# 커뮤니티 비밀번호가 일치하지 않을 때 사용하는 예외
class IncorrectPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="Forbidden; Incorrect community password provided in Authorization header."
        )