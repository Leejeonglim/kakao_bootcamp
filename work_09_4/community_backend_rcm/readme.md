# community_backend_rcm 디렉토리 생성
mkdir community_backend_rcm
cd community_backend_rcm

# 서브 디렉토리 생성
mkdir routes controllers models schemas exceptions

# 필요한 라이브러리 설치
# (fastapi, uvicorn[standard], pydantic 설치)
pip install fastapi uvicorn[standard] pydantic


# 서버실행
uvicorn main:app --reload




# 1. 오류 날 시 
# 현재 디렉터리(community_backend)에 어떤 가상 환경 폴더가 있는지 확인해 보세요
ls -F


source "가상환경이름"/bin/activate


# 2. 경로 오류
# 활성화 명령어를 실행할 때, 가상 환경 폴더(kakao_bootcamp)가 현재 작업 디렉터리(community_backend)의 바로 아래에 있어야 합니다.