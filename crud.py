from sqlalchemy.orm import Session
from datetime import date
from f18asilversurfers.routes.order import Order
def create_order(db: Session, customer_name: str, order_date: date):
    order = Order(customer_name=customer_name, order_date=order_date)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session):
    return db.query(Order).all()

def update_order(db: Session, order_id: int, customer_name: str = None, order_date: date = None):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        if customer_name:
            order.customer_name = customer_name
        if order_date:
            order.order_date = order_date
        db.commit()
        db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return order