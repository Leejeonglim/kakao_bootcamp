# 2-3 routes/community.py

from fastapi import APIRouter, Header, status
from controllers.community import get_all_posts_controller, create_post_controller
from models.community import PostCreate, PostResponse
from typing import List

router = APIRouter(
    prefix='/community',
    tags=['Community'],
)

# 1. 모든 게시글 목록 조회 라우트 (GET /community/)
# response_model로 응답 데이터 형식을 명시
@router.get(
    '/',
    response_model=List[PostResponse],
    summary='전체 게시글 목록 조회'
)

def get_all_posts_route():
    posts = get_all_posts_controller()
    return posts # Pydanic 모델 리스트를 반환하면 FastAPI가 자동으로 JSON으로 변환

# 2. 게시글 생성 라우트 (POST /community)
@router.post(
    '/',
    response_model=PostResponse,  # 성공 응답 모델
    status_code=status.HTTP_201_CREATED,
    summary='새 게시글 생성 (비밀번호 검증 필수)'
)

def create_post_route(
    post_data: PostCreate, # 요청 본문을 Pydantic 모델로 자동 검증
    authorization: str = Header(..., description='Community Password: start21')
):
    # 컨트롤러에서 발생할 수 있는 예외는 별도로 처리할 필요 없이
    # FastAPI의 기본 예외처리기가 담당합니다.
    new_post = create_post_controller(post_data, authorization)
    
    return new_post
