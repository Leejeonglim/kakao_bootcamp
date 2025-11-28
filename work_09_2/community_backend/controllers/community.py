# 2-3 controllers/community.py

from models.community import PostCreate, PostResponse
from exceptions.http_exceptions import IncorrectPasswordException

# 실제 데이터베이스 대신 메모리 내 더미 데이터 사용

DUMMY_POSTS = [
    {'id': 1, 'title': '첫 번째 게시글', 'content': 'FastAPI로 백엔드 시작!', 'author': 'admin'},
    {'id': 2, 'title': '안녕하세요', 'content': '커뮤니티 환영합니다.', 'author': 'guest'},
]

# 2-3에서 추가
COMMUNITY_PASSWORD = "start21" # 비밀번호 상수 정의

def get_all_posts_controller():
    '''모든 게시글 목록을 반환하는 컨트롤러 로직 '''
    # 여기서 실제 DM 쿼리, 캐시 확인 등의 비지니스 로직 수행
    return DUMMY_POSTS

def create_post_controller(post_data: dict, password: str):

    # 2-3 비밀번호 검증 (예외 발생)
    if password != COMMUNITY_PASSWORD:
        raise IncorrectPasswordException() # 사용자 정의 예외 발생
    
    # 2-3 데이터 처리
    new_id = max([p.id for p in DUMMY_POSTS])+1 if DUMMY_POSTS else 1

    new_post = PostResponse(
        id=new_id,
        title=post_data.title,
        content=post_data.content,
        author=post_data.author
    )    
    DUMMY_POSTS.append(new_post)
    
    return new_post