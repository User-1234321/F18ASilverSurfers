from pydantic import BaseModel
from typing import Optional

class DespatchAdvice(BaseModel):
    note: str
    despatch_advice_type: str  
    fulfillment: str  
    issue_date: str 
    quantity: int
    backorder: Optional[str] = None
    reason: str