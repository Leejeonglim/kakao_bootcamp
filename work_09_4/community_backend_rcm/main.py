# main.py (App Entry Point)

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from routes import community as community_routes
import uvicorn

# 1. FastAPI 애플리케이션 초기화
app = FastAPI(
    title="Community Backend (RCM Pattern)",
    description="Route-Controller-Model 패턴을 적용한 FastAPI 커뮤니티 백엔드입니다.",
    version="1.0.0"
)

# 2. 모든 HTTPException에 대한 전역 예외 핸들러 (필수조건 충족)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """커스텀 HTTP 예외(403, 404 등) 및 FastAPI 기본 예외 처리."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.detail},
    )

# 3. 라우터 포함
app.include_router(community_routes.router)

# 4. 기본 경로 라우트
@app.get("/")
def read_root():
    return {"success": True, "message": "Welcome to the RCM Community Backend! See /docs for API details."}

# 실행 (development only)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)