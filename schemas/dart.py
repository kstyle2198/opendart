from pydantic import BaseModel, Field, field_validator
from typing import Optional

class 공시검색Request(BaseModel):
    """
    공시 검색을 위한 요청 모델.

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
        bgn_de (str): 조회 시작일 (YYYYMMDD 형식, 예: 20260101)

    Validation:
        - bgn_de는 반드시 8자리 날짜(YYYYMMDD) 형식이어야 함.
    """
    corp_code: str = Field("01390344", description="기업 고유 코드")
    bgn_de: str = Field("20260101", description="조회 시작일 (YYYYMMDD)")

    @field_validator("bgn_de")
    def validate_date(cls, v):
        if len(v) != 8:
            raise ValueError("bgn_de must be YYYYMMDD")
        return v

class 기업개황Request(BaseModel):
    """
    기업 개황(기본 정보) 조회를 위한 요청 모델.

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
    """
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
    bsns_year : str = Field("2025", description="사업연도(YYYY)")
    reprt_code : str = Field("11011", description="보고서코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)")

    @field_validator("bsns_year")
    def validate_date(cls, v):
        if len(v) != 4:
            raise ValueError("bsns_year must be YYYY")
        return v
    
class 단일다중회사주요계정Request(BaseModel):
    """
    단일회사 및 다중회사 주요계정 조회를 위한 요청 모델

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
    bsns_year : str = Field("2025", description="사업연도(YYYY)")
    reprt_code : str = Field("11011", description="보고서코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)")
    
    @field_validator("bsns_year")
    def validate_date(cls, v):
        if len(v) != 4:
            raise ValueError("bsns_year must be YYYY")
        return v

class 단일회사전체재무재표Request(BaseModel):
    """
    단일회사전체재무재표 조회를 위한 요청 모델

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
        bsns_year (str): 사업연도 (YYYY 형식, 예: 2026)
        reprt_code (str): 보고서 코드
            - 11011: 사업보고서
            - 11012: 반기보고서
            - 11013: 1분기보고서
            - 11014: 3분기보고서
        fs_div (str): 개별/연결구분 
            - OFS:재무제표
            - CFS:연결재무제표

    Validation:
        - bsns_year는 반드시 4자리 연도(YYYY) 형식이어야 함.
    """
    corp_code: str = Field("01390344", description="기업 고유 코드")
    bsns_year : str = Field("2025", description="사업연도(YYYY)")
    reprt_code : str = Field("11011", description="보고서코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)")
    fs_div : str = Field("OFS", description="개별/연결구분 (OFS:재무제표, CFS:연결재무제표)")

    @field_validator("bsns_year")
    def validate_date(cls, v):
        if len(v) != 4:
            raise ValueError("bsns_year must be YYYY")
        return v
    
class 단일다중회사주요재무지표Request(BaseModel):
    """
    단일회사 및 다중회사 주요재무지표 조회를 위한 요청 모델

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
        bsns_year (str): 사업연도 (YYYY 형식, 예: 2026)
        reprt_code (str): 보고서 코드
            - 11011: 사업보고서
            - 11012: 반기보고서
            - 11013: 1분기보고서
            - 11014: 3분기보고서
        idx_cl_code (str): 지표분류코드 
            - 수익성지표 : M210000 
            - 안정성지표 : M220000 
            - 성장성지표 : M230000 
            - 활동성지표 : M240000

    Validation:
        - bsns_year는 반드시 4자리 연도(YYYY) 형식이어야 함.
    """
    corp_code: str = Field("01390344", description="기업 고유 코드")
    bsns_year : str = Field("2025", description="사업연도(YYYY)")
    reprt_code : str = Field("11011", description="보고서코드 (1분기보고서 : 11013, 반기보고서 : 11012, 3분기보고서 : 11014, 사업보고서 : 11011)")
    idx_cl_code : str = Field("M210000", description="지표분류코드 (수익성지표 : M210000 안정성지표 : M220000 성장성지표 : M230000 활동성지표 : M240000)")

    @field_validator("bsns_year")
    def validate_date(cls, v):
        if len(v) != 4:
            raise ValueError("bsns_year must be YYYY")
        return v
    
class 지분공시Request(BaseModel):
    """
    지분공시 조회를 위한 요청 모델.

    Attributes:
        corp_code (str): 기업 고유 코드 (예: 01390344)
    """
    corp_code: str = Field("01390344", description="기업 고유 코드")