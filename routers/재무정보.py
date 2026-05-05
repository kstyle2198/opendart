from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 단일다중회사주요계정Request, 단일회사전체재무재표Request, 단일다중회사주요재무지표Request
from services.dart_service import service_단일다중회사주요계정, service_단일회사전체재무재표, service_단일다중회사주요재무지표

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

재무정보router = APIRouter(prefix="/jemu_info", tags=["재무정보"])


@재무정보router.post("/fnlttSinglAcnt")
async def get_단일회사주요계정(req: 단일다중회사주요계정Request, request: Request):
    logger.info(f"Try for {get_단일회사주요계정}")
    BASE_URL= "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"
    try:
        return await service_단일다중회사주요계정(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@재무정보router.post("/fnlttMultiAcnt")
async def get_다중회사주요계정(req: 단일다중회사주요계정Request, request: Request):
    logger.info(f"Try for {get_다중회사주요계정}")
    BASE_URL= "https://opendart.fss.or.kr/api/fnlttMultiAcnt.json"
    try:
        return await service_단일다중회사주요계정(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@재무정보router.post("/fnlttSinglAcntAll")
async def get_단일회사전체재무재표(req: 단일회사전체재무재표Request, request: Request):
    logger.info(f"Try for {get_단일회사전체재무재표}")
    BASE_URL= "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
    try:
        return await service_단일회사전체재무재표(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@재무정보router.post("/fnlttSinglIndx")
async def get_단일회사주요재무지표(req: 단일다중회사주요재무지표Request, request: Request):
    logger.info(f"Try for {get_단일회사주요재무지표}")
    BASE_URL= "https://opendart.fss.or.kr/api/fnlttSinglIndx.json"
    try:
        return await service_단일다중회사주요재무지표(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@재무정보router.post("/prvsrpCptalUseDtls")
async def get_다중회사주요재무지표(req: 단일다중회사주요재무지표Request, request: Request):
    logger.info(f"Try for {get_다중회사주요재무지표}")
    BASE_URL= "https://opendart.fss.or.kr/api/prvsrpCptalUseDtls.json"
    try:
        return await service_단일다중회사주요재무지표(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

