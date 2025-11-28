# 2-1 main.py 하나에 라우트를 정의하여 Postman 요청에 응답하고, 기본 예외 처리를 포함합니다.

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn



# 비밀번호 정의 (2-1에서만 2-2부터는 정의할 필요 없음)
COMMUNITY_PASSWORD = 'start21'

# 1. FastAPI 애플리케이션 초기화
app = FastAPI(title='Community Backend (Route Only)')



# 2. 사용자 정의 예외 핸들러 (Exception Handler)
# 모든 HTTPException을 깔끔하게 응답
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # 표준 HTTP 예외 응답을 처리합니다.
    return JSONResponse(
        status_code=exc.status_code,
        content={'sucess': False, 'message': exc.detail},
    )
    
    
    
# 3. 루트 경로 라우트 정의 (GET /)
@app.get('/')
def read_root():
    # 기본 상태 확인 및 안내 메시지 반환
    return {
        'sucess' : True,
        'message' : "Welcome to the FastAPI Community Backend!"
        }
        

# 4. 상태 확인 라우트 (GET / status)
@app.get('/status')
def get_status():
    # 백엔드 상태 및 커뮤니티 비밀번호 정보를 반환합니다.
    return {
        'sucess' : True,
        'status' : 'Operatinal',
        'community_name' : 'FastAPI Community',
        'password_hint' : COMMUNITY_PASSWORD # 비밀번호 확인용
    }
    
# 5. 텍스트 라우트 (GET / test_error)
# 예외 처리 텍스트를 위한 라우트
@app.get('/test_error')
def test_error_handling():
    # 예외 처리기 테스트를 위해 404 Not Found 예외를 발생시킵니다.
    raise HTTPException(status_code=404, detail="Test Error: The requested resource was not found for testing purpose.")


# 2-1에서만 존채 2-2에선 삭제
# 6. 잘못된 요청 경로 처리 (모든 다른 경로에 대한 404 처리)
@app.middleware("http")
async def check_auth_middleware(request: Request, call_next):
    # 모든 요청에 대해 기본적인 인증 헤더를 확인합니다.
    # 실제 인증은 아닙니다. 예외 처리를 보여주기 위한 예시
    if request.url.path not in ["/", "/status"] and "authorization" not in request.headers:
        # 이 단계에서는 복잡한 예외처리 대신 기본 응답만
        pass
    
    response = await call_next(request)
    return response
'''


'''
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
