# 1. Python 베이스 이미지
FROM python:3.12-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. 의존성 파일 복사
COPY requirements.txt .

# 5. 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 6. 앱 소스 복사
COPY . .

# 7. 포트 오픈
EXPOSE 8000

# 8. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]