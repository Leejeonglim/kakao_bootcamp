# model_service.py (AI Model Loading and Prediction Logic)

from transformers import pipeline
from typing import Dict, Any
import torch

DEVICE = torch.device("cpu")
MODEL_ID = "monologg/koelectra-base-v3-naver-ner"

# 모델 로딩은 서버 시작 시 한 번만 수행
# 'monologg/koelectra-base-v3-discriminator-finetuned-nsmc' 모델 사용
try:
    # 텍스트 분류 파이프라인 초기화
    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model=MODEL_ID,
        device=DEVICE
    )
    print("AI Model loaded successfully.")
    
except Exception as e:
    # 모델 로딩 실패 시, 서버가 시작되지 않도록 예외 발생
    print(f"Error loading AI model: {e}")
    sentiment_pipeline = None


def predict_sentiment(text: str) -> Dict[str, Any]:
    # 주어진 텍스트에 대해 감성 분석을 수행하고 결과를 반환합니다.
    
    if sentiment_pipeline is None:
        raise RuntimeError("AI model is not available.")
        
    # 추론 수행
    result = sentiment_pipeline(text)[0]
    
    # 결과 포맷팅
    # LABEL_0: 부정 (Negative), LABEL_1: 긍정 (Positive)
    label = "Positive" if result['label'] == 'LABEL_1' else "Negative"
    
    return {
        "text": text,
        "sentiment": label,
        "confidence": result['score']
    }

# FastAPI에서 모델의 상태를 확인할 수 있는 함수
def get_model_status() -> bool:
    """모델 로딩 상태를 반환합니다."""
    return sentiment_pipeline is not None