from typing import Optional
from pydantic import BaseModel
from datetime import date

class DespatchAdvice(BaseModel):
    note: str
    despatch_advice_type: str
    fulfillment: str
    issue_date: date
    quantity: int
    backorder: Optional[int] = None
    reason: Optional[str] = None
