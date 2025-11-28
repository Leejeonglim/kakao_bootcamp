# exceptions/http_exceptions.py (Exception Layer)

from fastapi import HTTPException, status

class NotFoundException(HTTPException):
    """자원을 찾을 수 없을 때 발생하는 404 예외."""
    def __init__(self, resource_name: str = "Resource"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"{resource_name} not found."
        )

class IncorrectPasswordException(HTTPException):
    """비밀번호가 일치하지 않을 때 발생하는 403 예외."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Forbidden: Incorrect community password provided. (Password: start21)"
        )