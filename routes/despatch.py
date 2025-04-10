from contextlib import asynccontextmanager
from typing import Optional
from fastapi import APIRouter, FastAPI, HTTPException, Depends, Header, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from models import order_models

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/despatch_advices")
def get_all_despatch_advices(
    request: Request,
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    """Fetch all despatch advices from the database"""
    despatch_advices = db.query(order_models.DespatchAdviceDB).all()  # Query for despatch advice
    return despatch_advices

@router.get("/despatch_advice/{despatch_advice_id}")
def get_despatch_advice(despatch_id: int, db: Session = Depends(get_db)):
    """Fetch a single despatch advice by ID from the database"""
    despatch_advice = db.query(order_models.DespatchAdviceDB).filter(order_models.DespatchAdviceDB.id == despatch_id).first()
    if despatch_advice:
        return despatch_advice
    raise HTTPException(status_code=404, detail="Despatch advice not found")
