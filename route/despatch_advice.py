from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.schemas import DespatchAdvice, DespatchType, FulfillmentType
from models.crud import create_despatch_advice, get_all_despatch_advices
from models.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DespatchAdviceCreate(BaseModel):
    order_id: int
    despatch_type: DespatchType
    fulfillment: FulfillmentType

@router.post("/despatch_advice", response_model=DespatchAdvice)
def create_despatch_advice_route(
    despatch_advice_data: DespatchAdviceCreate, db: Session = Depends(get_db)
):

    despatch_advice = create_despatch_advice(
        db, despatch_advice_data.order_id, despatch_advice_data.despatch_type, despatch_advice_data.fulfillment
    )
    
    if not despatch_advice:
        raise HTTPException(
            status_code=404,
            detail=f"Order ID {despatch_advice_data.order_id} not found."
        )
    
    return despatch_advice

@router.get("/despatch_advices", response_model=list[DespatchAdvice])
def get_despatch_advices_route(db: Session = Depends(get_db)):
    return get_all_despatch_advices(db)
