from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 증권신고서Request
from services.dart_service import service_증권신고서

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

증권신고router = APIRouter(prefix="/stock_report", tags=["증권신고"])


@증권신고router.post("/estkRs")
async def get_지분증권(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_지분증권}")
    BASE_URL= "https://opendart.fss.or.kr/api/estkRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@증권신고router.post("/bdRs")
async def get_채무증권(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_채무증권}")
    BASE_URL= "https://opendart.fss.or.kr/api/bdRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@증권신고router.post("/stkdpRs")
async def get_증권예탁증권(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_증권예탁증권}")
    BASE_URL= "https://opendart.fss.or.kr/api/stkdpRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@증권신고router.post("/mgRs")
async def get_합병(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_합병}")
    BASE_URL= "https://opendart.fss.or.kr/api/mgRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@증권신고router.post("/extrRs")
async def get_주식포괄적교환이전(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_주식포괄적교환이전}")
    BASE_URL= "https://opendart.fss.or.kr/api/extrRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@증권신고router.post("/dvRs")
async def get_분할(req: 증권신고서Request, request: Request):
    logger.info(f"Try for {get_분할}")
    BASE_URL= "https://opendart.fss.or.kr/api/dvRs.json"
    try:
        return await service_증권신고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   