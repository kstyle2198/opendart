from pydantic import BaseModel, Field, field_validator
from typing import Optional

class 공시검색Request(BaseModel):
    corp_code: str = Field("01390344", description="기업 고유 코드")
    bgn_de: str = Field("20260101", description="조회 시작일 (YYYYMMDD)")

    @field_validator("bgn_de")
    def validate_date(cls, v):
        if len(v) != 8:
            raise ValueError("bgn_de must be YYYYMMDD")
        return v

class 기업개황Request(BaseModel):
    corp_code: str = Field("01390344", description="기업 고유 코드")

    
class 정기보고서Request(BaseModel):
    """
    정기보고서 조회를 위한 요청 모델.

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
        bsns_year (str): 사업연도 (YYYY 형식, 예: 2026)
        reprt_code (str): 보고서 코드
            - 11011: 사업보고서
            - 11012: 반기보고서
            - 11013: 1분기보고서
            - 11014: 3분기보고서

    Validation:
        - bsns_year는 반드시 4자리 연도(YYYY) 형식이어야 함.
    """
    corp_code: str = Field("01390344", description="기업 고유 코드")
    bsns_year : str = Field("2026", description="사업연도(YYYY)")
    reprt_code : str = Field("11011", description="보고서코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)")

    @field_validator("bsns_year")
    def validate_date(cls, v):
        if len(v) != 4:
            raise ValueError("bsns_year must be YYYY")
        return v