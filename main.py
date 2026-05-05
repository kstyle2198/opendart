import requests
import zipfile
import io
import httpx
import xml.etree.ElementTree as ET
import pandas as pd
import os

from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from typing import List

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

from dotenv import load_dotenv
load_dotenv()
# 환경 변수 읽기
OPENDART_API_KEY = os.getenv("OPENDART_API_KEY")

DATA_DIR = "./data"
DATA_PATH = f"{DATA_DIR}/기업별고유번호.csv"


# -----------------------------
# 1. OpenDART 다운로드 함수
# -----------------------------
def fetch_and_save_corps():
    """기업별 고유별호 목록 데이터를 가져오는 함수"""
    url = "https://opendart.fss.or.kr/api/corpCode.xml"
    params = {"crtfc_key": OPENDART_API_KEY}

    response = requests.get(url, params=params)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        xml_filename = z.namelist()[0]
        with z.open(xml_filename) as xml_file:
            xml_data = xml_file.read()

    root = ET.fromstring(xml_data)

    rows = []
    for corp in root.findall(".//list"):
        rows.append({
            "corp_code": corp.findtext("corp_code"),
            "corp_name": corp.findtext("corp_name"),
            "stock_code": corp.findtext("stock_code"),
            "modify_date": corp.findtext("modify_date"),
        })

    df = pd.DataFrame(rows)
    df.to_csv(DATA_PATH, encoding="utf-8-sig", index=False)

    return df


# -----------------------------
# 2. 로딩 함수
# -----------------------------
def load_corps():
    df = pd.read_csv(DATA_PATH, dtype={"corp_code": str, "stock_code": str})
    return df[df["stock_code"].notna()].copy()


# -----------------------------
# 3. 초기화 (핵심)
# -----------------------------
def initialize_data():
    # 1) 디렉토리 생성
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

    # 2) 파일 없으면 생성
    if not os.path.exists(DATA_PATH):
        df = fetch_and_save_corps()
        return df[df["stock_code"].notna()].copy()

    # 3) 파일 있으면 로딩
    return load_corps()


# -----------------------------
# 4. Lifespan
# -----------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("[LifeSpan] Initialize 기업별고유번호 Data")
        app.state.corps_df = initialize_data()
        app.state.client = httpx.AsyncClient(timeout=10.0)
    except Exception as e:
        # 🔥 초기화 실패하면 서버 죽이는게 맞음 (fail-fast)
        logger.error(f"초기 데이터 로딩 실패: {e}")
        raise RuntimeError(f"초기 데이터 로딩 실패: {e}")

    yield

    # shutdown
    app.state.corps_df = None
    await app.state.client.aclose()


app = FastAPI(lifespan=lifespan, version="0.1.1", description="서비스형 OPENDART API")

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 운영에서는 도메인 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# -----------------------------
# 6. 검색 API
# -----------------------------
@app.get("/corp/search", response_model=List[dict], tags=["기업별고유번호"])
def find_corps(corp_name: str):
    """기업명에 corp_name 글자가 포함된 기업들의 고유번호 조회 API"""
    logger.info(f"기업고유번호 조회: {corp_name}")
    corps_df = app.state.corps_df

    if corps_df is None:
        logger.warning("기업별고유번호 데이터가 없습니다.")
        raise HTTPException(status_code=500, detail="데이터 없음")

    filtered = corps_df[corps_df["corp_name"].str.contains(corp_name, case=False, na=False)][["corp_name", "corp_code"]]
    return filtered.to_dict(orient="records")

# -----------------------------
# Routers
# -----------------------------
from routers.공시정보 import 공시정보router
from routers.정기보고서 import 정기보고서router
from routers.재무정보 import 재무정보router
from routers.지분공시 import 지분공시router

app.include_router(공시정보router)
app.include_router(정기보고서router)
app.include_router(재무정보router)
app.include_router(지분공시router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)