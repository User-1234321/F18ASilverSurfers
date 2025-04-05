from fastapi import APIRouter, HTTPException, Response
from models.despatch_advice_models import DespatchAdvice
from dicttoxml import dicttoxml
from data.mock_orders import MOCK_ORDERS

router = APIRouter()

@router.post("/despatch-advice/{order_id}", response_class=Response)
def post_despatch_advice(order_id: int, advice: DespatchAdvice):
    """Post despatch advice for an order and return XML response"""
    order = MOCK_ORDERS.get(order_id)
    if order:
        order_dict = order.dict()
        order_dict["order_line"]["note"] = advice.note
        order_dict["despatch_advice_type"] = advice.despatch_advice_type
        order_dict["fulfillment"] = advice.fulfillment
        order_dict["issue_date"] = advice.issue_date
        order_dict["quantity"] = advice.quantity
        order_dict["backorder"] = advice.backorder
        order_dict["reason"] = advice.reason

        xml_data = dicttoxml(order_dict, custom_root="DespatchAdvice", attr_type=False)
        return Response(content=xml_data, media_type="application/xml")

    raise HTTPException(status_code=404, detail="Order not found")