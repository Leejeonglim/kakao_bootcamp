# schemas/community.py (Schema Layer: Pydantic Validation)

from pydantic import BaseModel, Field
from typing import Optional

class PostCreate(BaseModel):
    """게시글 생성 요청 시 필요한 데이터 모델 (입력 유효성 검사)."""
    title: str = Field(..., min_length=2, max_length=50, example="새로운 게시글 제목")
    content: str = Field(..., min_length=10, example="내용은 최소 10자 이상입니다.")
    author: Optional[str] = Field("Anonymous", max_length=20, example="작성자명")

class PostResponse(BaseModel):
    """게시글 응답 시 반환될 데이터 모델 (출력 형식 정의)."""
    id: int = Field(..., example=3)
    title: str
    content: str
    author: str