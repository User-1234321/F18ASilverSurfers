from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.schemas import Order
from models.database import SessionLocal, OrderDB
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#gets order from order_id

@router.get("/order/{order_ID}", response_model=Order)
def get_order(order_id: str, db: Session = Depends(get_db)):
    order = db.query(OrderDB).filter(OrderDB.order_id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not Found")
    return order




