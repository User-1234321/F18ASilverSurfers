from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from f18asilversurfers.database import SessionLocal
from f18asilversurfers.models import Order
from f18asilversurfers.models.order_models import OrderLine

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/orders")
def get_all_orders(db: Session = Depends(get_db)):
    """Fetch all orders from the database"""
    orders = db.query(Order).all()
    return orders

@router.get("/order/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Fetch a single order by ID from the database"""
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")
