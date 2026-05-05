from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 지분공시Request
from services.dart_service import service_지분공시

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

지분공시router = APIRouter(prefix="/gibun_info", tags=["지분공시"])


@지분공시router.post("/majorstock")
async def get_대량보유상황보고(req: 지분공시Request, request: Request):
    logger.info(f"Try for {get_대량보유상황보고}")
    BASE_URL= "https://opendart.fss.or.kr/api/majorstock.json"
    try:
        return await service_지분공시(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@지분공시router.post("/elestock")
async def get_임원주요주주소유보고(req: 지분공시Request, request: Request):
    logger.info(f"Try for {get_임원주요주주소유보고}")
    BASE_URL= "https://opendart.fss.or.kr/api/elestock.json"
    try:
        return await service_지분공시(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 