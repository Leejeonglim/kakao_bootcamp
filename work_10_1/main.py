# main.py (FastAPI App, Routing, and Exception Handling)

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from schemas import TextRequest, PredictionResponse, ErrorResponse
from model_service import predict_sentiment, get_model_status
import uvicorn
from typing import Dict, Any

# 1. FastAPI 애플리케이션 초기화
app = FastAPI(
    title="AI Sentiment Analysis Server",
    description="FastAPI를 사용한 텍스트 감성 분석 모델 서빙 예제",
    version="1.0.0"
)

# 2. 전역 예외 핸들러 (필수조건: 예외 처리)

# 2-1. 사용자 정의 HTTP 예외 처리 (4XX, 5XX)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # 모든 HTTPException (404, 422, 403 등)을 통일된 JSON 형식으로 처리합니다.
    
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            success=False, 
            message=exc.detail
        ).model_dump()
    )

# 2-2. 런타임 오류 (모델 로드 실패 등) 처리
@app.exception_handler(RuntimeError)
async def runtime_error_handler(request: Request, exc: RuntimeError):
    # Model Service에서 발생할 수 있는 런타임 오류 (예: 모델 사용 불가) 처리.
    
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, # 503 Service Unavailable
        content=ErrorResponse(
            success=False, 
            message=f"Model Service Error: {str(exc)}"
        ).model_dump()
    )

# 3. 라우트 정의

# 3-1. 상태 확인 라우트
@app.get(
    "/status", 
    summary="서버 및 모델 상태 확인",
    response_model=Dict[str, Any]
)
def get_status():
    # AI 모델 로딩 상태를 확인합니다.
    model_ok = get_model_status()
    
    return {
        "success": True,
        "server_status": "Operational",
        "model_loaded": model_ok,
        "message": "Model is ready for prediction." if model_ok else "Model failed to load."
    }

# 3-2. 예측(추론) 라우트
@app.post(
    "/predict", 
    summary="텍스트 감성 분석 예측",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK
)
async def predict_sentiment_route(request_data: TextRequest):
    # 입력된 텍스트에 대한 감성(Positive/Negative)을 예측합니다.
    # Pydantic TextRequest에 의해 입력 데이터 유효성 검사(422)가 자동 처리됩니다.
    
    try:
        # 모델 서비스 호출 (오류 발생 시 런타임 오류 핸들러로 이동)
        prediction_result = predict_sentiment(request_data.text)
        
        # Pydantic Response 모델을 사용하여 응답
        return prediction_result
        
    except RuntimeError as e:
        # 런타임 오류는 이미 전역 핸들러에 등록되어 있지만, 명시적으로 예외를 다시 발생시켜도 됨
        raise e
    except Exception as e:
        # 예측 중 예상치 못한 기타 오류 발생 시 500 에러 처리
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An unexpected error occurred during prediction: {str(e)}"
        )