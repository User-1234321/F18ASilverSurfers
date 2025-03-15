from sqlalchemy.orm import Session
from models.database import DespatchAdviceDB, OrderDB, DespatchType, FulfillmentType
from models.schemas import DespatchAdvice, Order

def create_despatch_advice(db: Session, order_id: int, despatch_type: DespatchType, fulfillment: FulfillmentType):
    order = db.query(OrderDB).filter(OrderDB.order_id == order_id).first()
    
    if order:
        despatch_advice = DespatchAdviceDB(
            despatch_type=despatch_type,
            fulfillment=fulfillment,
            order_id=order.order_id
        )
        db.add(despatch_advice)
        db.commit()
        db.refresh(despatch_advice)
        
        return DespatchAdvice(
            order=Order(
                order_id=order.order_id,
                buyer_id=order.buyer_id,
                buyer_address=order.buyer_address,
                buyer_contact=order.buyer_contact,
                seller_id=order.seller_id,
                seller_address=order.seller_address,
                seller_contact=order.seller_contact,
                delivery_address=order.delivery_address,
                requested_delivery_period=order.requested_delivery_period,
                transaction_conditions=order.transaction_conditions,
            ),
            despatch_type=despatch_advice.despatch_type,
            fulfillment=despatch_advice.fulfillment,
        )
    return None

def get_all_despatch_advices(db: Session):
    despatch_advices = db.query(DespatchAdviceDB).all()
    return [
        DespatchAdvice(
            order=Order(
                order_id=adv.order.order_id,
                buyer_id=adv.order.buyer_id,
                buyer_address=adv.order.buyer_address,
                buyer_contact=adv.order.buyer_contact,
                seller_id=adv.order.seller_id,
                seller_address=adv.order.seller_address,
                seller_contact=adv.order.seller_contact,
                delivery_address=adv.order.delivery_address,
                requested_delivery_period=adv.order.requested_delivery_period,
                transaction_conditions=adv.order.transaction_conditions,
            ),
            despatch_type=adv.despatch_type,
            fulfillment=adv.fulfillment,
        )
        for adv in despatch_advices
    ]
