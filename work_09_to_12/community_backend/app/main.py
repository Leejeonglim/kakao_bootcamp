# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .db import Base, engine
from .routes.post_routes import router as post_router
from .utils.exceptions import register_exception_handlers
from . import models  # noqa: F401 (Base에 모델 등록용)


app = FastAPI(title="Community Backend (Route-Controller-Model)")

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

# 정적 파일 (프론트엔드)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 라우터 등록
app.include_router(post_router)

# 예외 핸들러 등록
register_exception_handlers(app)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/")
async def root():
    # 프론트 메인 페이지
    return FileResponse("app/static/index.html")
