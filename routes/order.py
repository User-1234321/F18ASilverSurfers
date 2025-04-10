from contextlib import asynccontextmanager
from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException, Depends, Header, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from models import the_models

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/orders")
def get_all_orders(
    request: Request,
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    """fake shit for testing"""
    orders = db.query(the_models.Order).all()
    print(orders)
    return orders  # <== Add this


@router.get("/order/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Fetch a single order by ID from the database"""
    order = db.query(the_models.Order).filter(the_models.Order.id == order_id).first()  # Corrected here
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")