# controllers/community.py (Step 2-2: Controller with Dummy Logic)

# 실제 데이터베이스 대신 메모리 내 더미 데이터 사용
DUMMY_POSTS = [
    {"id": 1, "title": "첫 번째 게시글", "content": "FastAPI로 백엔드 시작!", "author": "admin"},
    {"id": 2, "title": "안녕하세요", "content": "커뮤니티 환영합니다.", "author": "guest"},
]

def get_all_posts_controller():
    """
    모든 게시글 목록을 반환하는 컨트롤러 로직 (현재는 더미 데이터).
    """
    # 여기서 실제 DB 쿼리, 캐시 확인 등의 비즈니스 로직 수행
    return DUMMY_POSTS

def create_post_controller(post_data: dict, password: str):
    """
    새 게시글을 생성하는 컨트롤러 로직.
    비밀번호를 검증하고, 성공 시 새 게시글을 반환합니다.
    """
    # 실제 커뮤니티 비밀번호 검증
    if password != "start21":
        # 403 Forbidden 예외를 발생시키도록 라우트에서 처리해야 합니다.
        # 컨트롤러는 데이터 처리에 집중하고, HTTP 예외 처리는 라우트에서 분리
        return None # 실패 시 None 반환
    
    # 새 게시글 ID 생성 (단순 증가)
    new_id = len(DUMMY_POSTS) + 1
    new_post = {
        "id": new_id, 
        "title": post_data["title"], 
        "content": post_data["content"], 
        "author": post_data.get("author", "Anonymous")
    }
    DUMMY_POSTS.append(new_post)
    
    return new_post