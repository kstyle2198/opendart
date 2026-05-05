from fastapi import APIRouter, Request, HTTPException
from schemas.dart import 주요사항Request
from services.dart_service import service_주요사항

from utils.setlogger import setup_logger
logger = setup_logger(log_name="opendart")

주요사항router = APIRouter(prefix="/major_event", tags=["주요사항보고서"])


@주요사항router.post("/astInhtrfEtcPtbkOpt")
async def get_자산양수도풋백옵션(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_자산양수도풋백옵션}")
    BASE_URL= "https://opendart.fss.or.kr/api/astInhtrfEtcPtbkOpt.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/dfOcr")
async def get_부도발생(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_부도발생}")
    BASE_URL= "https://opendart.fss.or.kr/api/dfOcr.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/bsnSp")
async def get_영업정지(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_영업정지}")
    BASE_URL= "https://opendart.fss.or.kr/api/bsnSp.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/ctrcvsBgrq")
async def get_회생절차개시신청(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_회생절차개시신청}")
    BASE_URL= "https://opendart.fss.or.kr/api/ctrcvsBgrq.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/dsRsOcr")
async def get_해산사유발생(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_해산사유발생}")
    BASE_URL= "https://opendart.fss.or.kr/api/dsRsOcr.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/piicDecsn")
async def get_유상증자결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_유상증자결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/piicDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/fricDecsn")
async def get_무상증자결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_무상증자결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/fricDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/pifricDecsn")
async def get_유무상증자결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_유무상증자결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/pifricDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/crDecsn")
async def get_감자결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_감자결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/crDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/bnkMngtPcbg")
async def get_채권은행관리개시(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_채권은행관리개시}")
    BASE_URL= "https://opendart.fss.or.kr/api/bnkMngtPcbg.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/lwstLg")
async def get_소송등의제기(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_소송등의제기}")
    BASE_URL= "https://opendart.fss.or.kr/api/lwstLg.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/ovLstDecsn")
async def get_해외증권시장주권상장결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_해외증권시장주권상장결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/ovLstDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/ovDlstDecsn")
async def get_해외증권시장주권상장폐지결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_해외증권시장주권상장폐지결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/ovDlstDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/ovLst")
async def get_해외증권시장주권등상장(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_해외증권시장주권등상장}")
    BASE_URL= "https://opendart.fss.or.kr/api/ovLst.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/ovDlst")
async def get_해외증권시장주권등상장폐지(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_해외증권시장주권등상장폐지}")
    BASE_URL= "https://opendart.fss.or.kr/api/ovDlst.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/cvbdIsDecsn")
async def get_전환사채발행결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_전환사채발행결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/cvbdIsDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/bdwtIsDecsn")
async def get_신주인수권부사채발행결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_신주인수권부사채발행결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/bdwtIsDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/exbdIsDecsn")
async def get_교환사채발행결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_교환사채발행결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/exbdIsDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/bnkMngtPcsp")
async def get_채권은행의관리절차중단(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_채권은행의관리절차중단}")
    BASE_URL= "https://opendart.fss.or.kr/api/bnkMngtPcsp.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/wdCocobdIsDecsn")
async def get_상각형조건부자본증권발행결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_상각형조건부자본증권발행결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/wdCocobdIsDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/tsstkAqDecsn")
async def get_자기주식취득결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_자기주식취득결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/tsstkAqDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@주요사항router.post("/tsstkAqTrctrCcDecsn")
async def get_자기주식취득신탁계약해지결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_자기주식취득신탁계약해지결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/tsstkAqTrctrCcDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/bsnInhDecsn")
async def get_영업양수결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_영업양수결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/bsnInhDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/bsnTrfDecsn")
async def get_영업양도결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_영업양도결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/bsnTrfDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/tgastInhDecsn")
async def get_유형자산양수결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_유형자산양수결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/tgastInhDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/tgastTrfDecsn")
async def get_유형자산양도결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_유형자산양도결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/tgastTrfDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/otcprStkInvscrInhDecsn")
async def get_타법인주식출자증권양수결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_타법인주식출자증권양수결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/otcprStkInvscrInhDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/otcprStkInvscrTrfDecsn")
async def get_타법인주식출자증권양도결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_타법인주식출자증권양도결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/otcprStkInvscrTrfDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/stkrtbdInhDecsn")
async def get_주권관련사채권양수결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_주권관련사채권양수결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/stkrtbdInhDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/stkrtbdTrfDecsn")
async def get_주권관련사채권양도결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_주권관련사채권양도결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/stkrtbdTrfDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/cmpMgDecsn")
async def get_회사합병결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_회사합병결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/cmpMgDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/cmpDvDecsn")
async def get_회사분할결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_회사분할결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/cmpDvDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/cmpDvmgDecsn")
async def get_회사분할합병결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_회사분할합병결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/cmpDvmgDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@주요사항router.post("/stkExtrDecsn")
async def get_주식교환이전결정(req: 주요사항Request, request: Request):
    logger.info(f"Try for {get_주식교환이전결정}")
    BASE_URL= "https://opendart.fss.or.kr/api/stkExtrDecsn.json"
    try:
        return await service_주요사항(request.app.state.client, req, BASE_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))