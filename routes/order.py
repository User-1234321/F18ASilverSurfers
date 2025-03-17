from fastapi import APIRouter, HTTPException
from data.mock_orders import MOCK_ORDERS

router = APIRouter()

@router.get("/orders")
def get_all_orders():
    """Fetch all mock orders"""
    return list(MOCK_ORDERS.values())

@router.get("/order/{order_id}")
def get_order(order_id: int):
    """Fetch a single mock order using ID"""
    order = MOCK_ORDERS.get(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")