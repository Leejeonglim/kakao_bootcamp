# 커뮤니티 게시판 프로젝트

FastAPI 기반 Route-Controller-Model 패턴과 SQLite(DB),  
그리고 바닐라 JS 프론트엔드로 구현한 간단 커뮤니티 게시판입니다.

## 1. 기술 스택

- Backend: FastAPI, Python, SQLAlchemy, SQLite
- Frontend: HTML, CSS, Vanilla JavaScript (Fetch API)
- Tool: Postman, Git, GitHub

## 2. 주요 기능

- 게시글 생성 (제목, 작성자, 내용)
- 게시글 목록 조회
- 게시글 상세 조회
- 게시글 삭제
- 웹 프론트엔드에서 REST API 호출

## 3. 아키텍처

- Route (`app/routes/post_routes.py`)
- Controller (`app/controllers/post_controller.py`)
- Model & CRUD (`app/models/post_model.py`)
- Schema (`app/schemas/post_schema.py`)
- DB 세팅 (`app/db.py`)
- 전역 예외 처리 (`app/utils/exceptions.py`)
- 프론트엔드 (`app/static/`)

## 4. 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload
