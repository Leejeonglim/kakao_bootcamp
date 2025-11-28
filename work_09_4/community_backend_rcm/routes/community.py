# routes/community.py (Route Layer: HTTP Endpoint Definition)

from fastapi import APIRouter, Header, status, Path
from controllers import community as community_controller
from schemas.community import PostCreate, PostResponse
from typing import List

router = APIRouter(
    prefix="/community",
    tags=["Community (RCM Pattern)"],
)

# 1. 전체 게시글 목록 조회 (GET /community/)
@router.get(
    "/",
    response_model=List[PostResponse],
    summary="전체 게시글 목록 조회",
)
def get_all_posts_route():
    """Controller를 호출하여 게시글 목록을 가져옵니다."""
    return community_controller.get_all_posts_controller()

# 2. 특정 게시글 상세 조회 (GET /community/{post_id})
@router.get(
    "/{post_id}",
    response_model=PostResponse,
    summary="특정 게시글 상세 조회 (404 예외 처리)",
)
def get_post_detail_route(
    post_id: int = Path(..., description="조회할 게시글의 ID", gt=0) # Path 검증 포함
):
    """Controller를 호출하여 특정 게시글을 가져옵니다. 게시글이 없으면 404 예외 발생."""
    return community_controller.get_post_detail_controller(post_id)

# 3. 새 게시글 생성 (POST /community/)
@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
    summary="새 게시글 생성 (403 비밀번호 예외 처리)",
)
def create_post_route(
    post_data: PostCreate, # Pydantic 입력 유효성 검사
    authorization: str = Header(..., description="Community Password: start21"),
):
    """Controller를 호출하여 게시글을 생성합니다. 비밀번호 오류 시 403 예외 발생."""
    # Controller에서 발생한 예외(403)는 FastAPI가 자동으로 처리합니다.
    return community_controller.create_post_controller(post_data, authorization)