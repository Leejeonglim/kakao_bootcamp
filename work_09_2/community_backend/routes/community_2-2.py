# 2-2 routes/community.py

from fastapi import APIRouter, HTTPException, Header
from controllers.community import get_all_posts_controller, create_post_controller

# 라우터 인스턴스 생성
router = APIRouter(
    perfix='/community',   # 이 라우터의 모든 경로 앞에 '/community'가 붙습니다.
    tags=['Community'],    # 문서화에 사용될 태그
)

# 1. 모든 게시글 목록 조회 라우트 (GET /community/)
@router.get('/')
def get_all_posts_route():
    '''
    모든 게시글 목록을 조회합니다.
    '''
    posts = get_all_posts_controller()
    return {'sucess': True, 'data': posts}

# 2. 게시글 생성 라우트 (POST /community/)
@router.post('/')
def create_post_route(post_data: dict, authorization: str = Header(..., description="Community Password: start21")):
    '''
    새 게시글을 생성합니다.
    요청 헤더의 'Authorization'에 커뮤니티 비밀번호가 포함되어야 합니다.
    '''
    password = authorization # Header의 값을 비밀번호로 사용
    
    # 컨트롤러 호출 및 비밀번호 검증
    new_post = create_post_controller(post_data, password)
    
    if new_post is None:
        # 필수조건: 예외 처리
        raise HTTPException(
            status_code=403,
            detail="Forbidden; Incorrect community password provided in Authorization header." 
        )
        
    return {'sucess': True, 'message': 'Post created sucessfully.', 'data': new_post}
