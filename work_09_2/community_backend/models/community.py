# 2-3 models/community.py

from pydantic import BaseModel, Field
from typing import Optional

# 게시글 생성 요청 모델
class PostCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=50, example='제목입니다.')
    content: str = Field(..., min_length=10, example='게시글 내용입니다.')
    author: Optional[str] = Field('Anonymous', max_length=20, example='작성자 이름')
    
    
# 게시글 응답 모델 (ID 포함)
class PostResponse(BaseModel):
    id: int = Field(..., example=1)
    title: str
    content: str
    author: str
    
