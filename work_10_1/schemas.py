# schemas.py (Pydantic Models for Validation and Response)

from pydantic import BaseModel, Field
from typing import Literal

# 1. 요청 모델 (Input Schema)
class TextRequest(BaseModel):
    """클라이언트로부터 텍스트를 입력받는 모델."""
    text: str = Field(..., min_length=5, max_length=500, example="이 영화 정말 재미있고 감동적이었어요!")

# 2. 응답 모델 (Output Schema)
class PredictionResponse(BaseModel):
    """감성 분석 결과를 반환하는 모델."""
    text: str
    sentiment: str = Field(..., example="Positive")
    confidence: float = Field(..., ge=0.0, le=1.0, example=0.987)

# 3. 오류 응답 모델 (Error Schema)
class ErrorResponse(BaseModel):
    success: Literal[False] = False
    message: str