from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class DespatchType(str, Enum):
    DELIVERY = "Delivery"
    RETURN = "Return"
    CANCEL = "Cancel"

class FulfillmentType(str, Enum):
    FULL = "Full"
    PARTIAL = "Partial"

class Buyer(BaseModel):
    id: int
    postal_address: str
    contact: str

class Seller(BaseModel):
    id: int
    postal_address: str
    contact: str

class Delivery(BaseModel):
    postal_address: str
    requested_delivery_period: str
    transaction_conditions: str

class OrderLine(BaseModel):
    note: str
    id: int

class Order(BaseModel):
    order_id: int
    buyer: Buyer
    seller: Seller
    delivery: Delivery
    order_lines: List[OrderLine]

class DespatchAdvice(BaseModel):
    order: Order
    despatch_type: DespatchType
    fulfillment: FulfillmentType

    class Config:
        orm_mode = True