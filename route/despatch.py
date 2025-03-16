from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.schemas import DespatchAdvice
from models.database import SessionLocal, DespatchAdviceDB, OrderDB
from pydantic import BaseModel 

router = APIRouter()

class DespatchAdviceCreate(BaseModel):
    ubl_version_id: str
    customization_id: str
    profile_id: str
    sales_order_id: str 
    copy_indicator: bool
    uuid: str
    document_status_code: str
    despatch_advice_type_code: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#

@router.post("/despatch_advice/", response_model=DespatchAdvice)
def create_despatch_advice(advice: DespatchAdvice, db: Session = Depends(get_db)):

    existing = db.query(OrderDB).filter(OrderDB.order_id == advice.sales_order_id).first()

    if not existing:
        raise HTTPException(status_code=400, detail="invalid sales_order_id: Order does not exist")
    
    new_Advice = DespatchAdviceDB(
        ubl_version_id=advice.ubl_version_id,
        customization_id=advice.customization_id,
        profile_id=advice.profile_id,
        sales_order_id=advice.sales_order_id,  
        copy_indicator=advice.copy_indicator,
        uuid=advice.uuid,
        document_status_code=advice.document_status_code,
        despatch_advice_type_code=advice.despatch_advice_type_code,
    )

    db.add(new_Advice)
    db.commit()
    db.refresh(new_Advice)

    return new_Advice
