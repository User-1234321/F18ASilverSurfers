from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from models.despatch_advice_models import DespatchAdvice
from database import SessionLocal  # Ensure you're importing the database session
from models import order_models
from dicttoxml import dicttoxml
from typing import Optional

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/despatch-advice/{order_id}", response_class=Response)
def post_despatch_advice(
    order_id: int, 
    advice: DespatchAdvice, 
    db: Session = Depends(get_db)
):
    """Post despatch advice for an order and return XML response"""
    
    # Fetch the order from the database
    order = db.query(order_models.Order).filter(order_models.Order.id == order_id).first()
    
    if order:
        # Convert the order to a dictionary (you can manually map the attributes to avoid errors with SQLAlchemy objects)
        order_dict = {
            "id": order.id,
            "ubl_version_id": order.ubl_version_id,
            "customization_id": order.customization_id,
            "profile_id": order.profile_id,
            "sales_order_id": order.sales_order_id,
            "copy_indicator": order.copy_indicator,
            "uuid": str(order.uuid),  # Convert UUID to string
            "issue_date": order.issue_date,
            "note": order.note,
            "buyer_customer_party_id": order.buyer_customer_party_id,
            "seller_supplier_party_id": order.seller_supplier_party_id,
            "originator_customer_party_id": order.originator_customer_party_id,
            "delivery_id": order.delivery_id,
            "delivery_terms_id": order.delivery_terms_id,
            "transaction_conditions_id": order.transaction_conditions_id,
            "anticipated_monetary_total_id": order.anticipated_monetary_total_id,
            "order_line_id": order.order_line_id
        }

        # Update the order dictionary with the despatch advice data
        order_dict["order_line"] = {
            "note": advice.note
        }
        order_dict["despatch_advice_type"] = advice.despatch_advice_type
        order_dict["fulfillment"] = advice.fulfillment
        order_dict["issue_date"] = advice.issue_date
        order_dict["quantity"] = advice.quantity
        order_dict["backorder"] = advice.backorder
        order_dict["reason"] = advice.reason

        # Convert the dictionary to XML
        xml_data = dicttoxml(order_dict, custom_root="DespatchAdvice", ids=False)

        # Return the XML response
        return Response(content=xml_data, media_type="application/xml")
    
    # Raise a 404 error if the order isn't found
    raise HTTPException(status_code=404, detail="Order not found")