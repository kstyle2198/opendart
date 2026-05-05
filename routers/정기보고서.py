from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 정기보고서Request
from services.dart_service import service_정기보고서

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

정기보고서router = APIRouter(prefix="/junggi_report", tags=["정기보고서"])

   
@정기보고서router.post("/irdsSttus")
async def get_증감자현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_증감자현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/irdsSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@정기보고서router.post("/alotMatter")
async def get_배당현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_배당현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/alotMatter.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@정기보고서router.post("/tesstkAcqsDspsSttus")
async def get_자기주식취득현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_자기주식취득현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/tesstkAcqsDspsSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@정기보고서router.post("/hyslrSttus")
async def get_최대주주현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_최대주주현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/hyslrSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@정기보고서router.post("/hyslrhyslrChgSttusSttus")
async def get_최대주주변동현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_최대주주변동현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/hyslrChgSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/exctvSttus")
async def get_임원현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_임원현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/exctvSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/empSttus")
async def get_직원현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_직원현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/empSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/hmvAuditIndvdlBySttus")
async def get_이사감사개인별보수현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_이사감사개인별보수현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/hmvAuditIndvdlBySttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/hmvAuditAllSttus")
async def get_이사감사전체보수현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_이사감사전체보수현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/hmvAuditAllSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/indvdlByPay")
async def get_개인별보수현황_top5(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_개인별보수현황_top5}")
    BASE_URL= "https://opendart.fss.or.kr/api/indvdlByPay.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/otrCprInvstmntSttus")
async def get_타법인출자현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_타법인출자현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/otrCprInvstmntSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/stockTotqySttus")
async def get_주식총수현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_주식총수현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/stockTotqySttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/detScritsIsuAcmslt")
async def get_채무증권발행실적(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_채무증권발행실적}")
    BASE_URL= "https://opendart.fss.or.kr/api/detScritsIsuAcmslt.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/entrprsBilScritsNrdmpBlce")
async def get_어음미상환잔액(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_어음미상환잔액}")
    BASE_URL= "https://opendart.fss.or.kr/api/entrprsBilScritsNrdmpBlce.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/srtpdPsndbtNrdmpBlce")
async def get_단기사채미상환잔액(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_단기사채미상환잔액}")
    BASE_URL= "https://opendart.fss.or.kr/api/srtpdPsndbtNrdmpBlce.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/cprndNrdmpBlce")
async def get_회사채미상환잔액(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_회사채미상환잔액}")
    BASE_URL= "https://opendart.fss.or.kr/api/cprndNrdmpBlce.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/newCaplScritsNrdmpBlce")
async def get_신종자본미상환잔액(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_신종자본미상환잔액}")
    BASE_URL= "https://opendart.fss.or.kr/api/newCaplScritsNrdmpBlce.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@정기보고서router.post("/cndlCaplScritsNrdmpBlce")
async def get_조건부자본미상환잔액(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_조건부자본미상환잔액}")
    BASE_URL= "https://opendart.fss.or.kr/api/cndlCaplScritsNrdmpBlce.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/accnutAdtorNmNdAdtOpinion")
async def get_감사의견(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_감사의견}")
    BASE_URL= "https://opendart.fss.or.kr/api/accnutAdtorNmNdAdtOpinion.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/adtServcCnclsSttus")
async def get_감사용역체결현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_감사용역체결현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/adtServcCnclsSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/accnutAdtorNonAdtServcCnclsSttus")
async def get_비감사용역체결현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_비감사용역체결현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/accnutAdtorNonAdtServcCnclsSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/outcmpnyDrctrNdChangeSttus")
async def get_사외이사현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_사외이사현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/outcmpnyDrctrNdChangeSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@정기보고서router.post("/unrstExctvMendngSttus")
async def get_미등기임원보수현황(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_미등기임원보수현황}")
    BASE_URL= "https://opendart.fss.or.kr/api/unrstExctvMendngSttus.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/drctrAdtAllMendngSttusGmtsckConfmAmount")
async def get_이사감사전체보수현황_주총승인(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_이사감사전체보수현황_주총승인}")
    BASE_URL= "https://opendart.fss.or.kr/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/drctrAdtAllMendngSttusMendngPymntamtTyCl")
async def get_이사감사전체보수현황_유형별(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_이사감사전체보수현황_유형별}")
    BASE_URL= "https://opendart.fss.or.kr/api/drctrAdtAllMendngSttusMendngPymntamtTyCl.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/pssrpCptalUseDtls")
async def get_공모자금사용내역(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_공모자금사용내역}")
    BASE_URL= "https://opendart.fss.or.kr/api/pssrpCptalUseDtls.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@정기보고서router.post("/prvsrpCptalUseDtls")
async def get_사모자금사용내역(req: 정기보고서Request, request: Request):
    logger.info(f"Try for {get_사모자금사용내역}")
    BASE_URL= "https://opendart.fss.or.kr/api/prvsrpCptalUseDtls.json"
    try:
        return await service_정기보고서(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
