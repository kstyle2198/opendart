from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 공시검색Request, 기업개황Request
from services.dart_service import service_공시검색, service_기업개황

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

공시정보router = APIRouter(prefix="/gongsi_info", tags=["공시정보"])


@공시정보router.post("/list")
async def get_공시검색(req: 공시검색Request, request: Request):
    logger.info(f"Try for {get_공시검색}")
    BASE_URL= "https://opendart.fss.or.kr/api/list.json"
    try:
        return await service_공시검색(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@공시정보router.post("/company")
async def get_기업개황(req: 기업개황Request, request: Request):
    logger.info(f"Try for {get_기업개황}")
    BASE_URL= "https://opendart.fss.or.kr/api/company.json"
    try:
        return await service_기업개황(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
 