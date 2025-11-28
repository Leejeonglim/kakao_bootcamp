# 2-1 main.py 하나에 라우트를 정의하여 Postman 요청에 응답하고, 기본 예외 처리를 포함합니다.

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from routes import community   # routes/community.py에서 router import 


# 1. FastAPI 애플리케이션 초기화
app = FastAPI(title='Community Backend (Route/Controller Seperate)')


# 2. 사용자 정의 예외 핸들러 (Exception Handler)
# 모든 HTTPException을 깔끔하게 응답
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # 표준 HTTP 예외 응답을 처리합니다.
    return JSONResponse(
        status_code=exc.status_code,
        content={'sucess': False, 'message': exc.detail},
    )
    
# 2-1>2-2 핵심 변경 사항 : 라우터 포함
app.include_router(community.router)  # routes/community.py의 router 포함

    
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
        #'community_name' : 'FastAPI Community',
        #'password_hint' : COMMUNITY_PASSWORD # 비밀번호 확인용
        'modules': ['community_router']
    }
    
# 5. 텍스트 라우트 (GET / test_error)
# 예외 처리 텍스트를 위한 라우트
@app.get('/test_error')
def test_error_handling():
    # 예외 처리기 테스트를 위해 404 Not Found 예외를 발생시킵니다.
    raise HTTPException(status_code=404, detail="Test Error: The requested resource was not found for testing purpose.")


