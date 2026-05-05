import os
from fastapi import HTTPException

OPENDART_API_KEY = os.getenv("OPENDART_API_KEY")


async def service_공시검색(client, req, BASE_URL):
    params = {
        "crtfc_key": OPENDART_API_KEY,
        "corp_code": req.corp_code,
        "bgn_de": req.bgn_de
    }

    try:
        response = await client.get(BASE_URL, params=params, timeout=10.0)

        # 1. HTTP 에러
        response.raise_for_status()

    except client.ConnectTimeout:
        raise HTTPException(status_code=504, detail="외부 API 연결 타임아웃")

    except client.RequestError as e:
        raise HTTPException(status_code=502, detail=f"외부 API 요청 실패: {str(e)}")

    except client.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"외부 API HTTP 오류: {e.response.text}"
        )

    # 2. JSON 파싱 에러
    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="JSON 파싱 실패")

    # 3. OpenDART 자체 에러 처리
    # 정상: status == '000'
    if data.get("status") != "000":
        raise HTTPException(
            status_code=400,
            detail=f"DART API 오류: {data.get('message')}"
        )

    return data


async def service_기업개황(client, req, BASE_URL):
    params = {
        "crtfc_key": OPENDART_API_KEY,
        "corp_code": req.corp_code,
    }

    try:
        response = await client.get(BASE_URL, params=params, timeout=10.0)

        # 1. HTTP 에러
        response.raise_for_status()

    except client.ConnectTimeout:
        raise HTTPException(status_code=504, detail="외부 API 연결 타임아웃")

    except client.RequestError as e:
        raise HTTPException(status_code=502, detail=f"외부 API 요청 실패: {str(e)}")

    except client.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"외부 API HTTP 오류: {e.response.text}"
        )

    # 2. JSON 파싱 에러
    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="JSON 파싱 실패")

    # 3. OpenDART 자체 에러 처리
    # 정상: status == '000'
    if data.get("status") != "000":
        raise HTTPException(
            status_code=400,
            detail=f"DART API 오류: {data.get('message')}"
        )

    return data


async def service_정기보고서(client, req, BASE_URL):
    params = {
        "crtfc_key": OPENDART_API_KEY,
        "corp_code": req.corp_code,
        "bsns_year": req.bsns_year,
        "reprt_code": req.reprt_code
    }

    try:
        response = await client.get(BASE_URL, params=params, timeout=10.0)

        # 1. HTTP 에러
        response.raise_for_status()

    except client.ConnectTimeout:
        raise HTTPException(status_code=504, detail="외부 API 연결 타임아웃")

    except client.RequestError as e:
        raise HTTPException(status_code=502, detail=f"외부 API 요청 실패: {str(e)}")

    except client.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"외부 API HTTP 오류: {e.response.text}"
        )

    # 2. JSON 파싱 에러
    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="JSON 파싱 실패")

    # 3. OpenDART 자체 에러 처리
    # 정상: status == '000'
    if data.get("status") != "000":
        raise HTTPException(
            status_code=400,
            detail=f"DART API 오류: {data.get('message')}"
        )

    return data