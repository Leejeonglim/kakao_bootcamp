# models/community_model.py (Model Layer: JSON Data Management)

# DB 역할을 대신하는 메모리 내 JSON(Dictionary) 리스트
_POSTS_DATA = [
    {"id": 1, "title": "RCM 패턴 첫 게시글", "content": "FastAPI로 아키텍처 구현 중!", "author": "admin"},
    {"id": 2, "title": "Model 계층 분리", "content": "JSON 데이터로 DB 역할 대체.", "author": "dev"},
]

COMMUNITY_PASSWORD = "start21"

# --- CRUD Operations (DB Functions) ---

def get_all_posts() -> list[dict]:
    """모든 게시글 목록을 JSON 형식(dict 리스트)으로 반환합니다."""
    return _POSTS_DATA

def get_post_by_id(post_id: int) -> dict | None:
    """ID에 해당하는 게시글을 찾아 JSON 형식(dict)으로 반환합니다."""
    for post in _POSTS_DATA:
        if post["id"] == post_id:
            return post
    return None

def create_post(post_data: dict) -> dict:
    """새 게시글을 생성하고 JSON 형식(dict)으로 반환합니다."""
    # 새 ID 생성
    max_id = max([p["id"] for p in _POSTS_DATA]) if _POSTS_DATA else 0
    new_id = max_id + 1
    
    new_post = {
        "id": new_id,
        "title": post_data["title"],
        "content": post_data["content"],
        "author": post_data.get("author", "Anonymous")
    }
    _POSTS_DATA.append(new_post)
    return new_post