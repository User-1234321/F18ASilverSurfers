from sqlalchemy.orm import Session
from datetime import date
from models.models import Order

def create_order(
    db,
    id,
    ubl_version_id,
    customization_id,
    profile_id,
    sales_order_id,
    copy_indicator,
    uuid,
    issue_date,
    note,
    buyer_customer_party_id,
    seller_supplier_party_id,
    originator_customer_party_id,
    delivery_id,
    delivery_terms_id,
    transaction_conditions_id,
    anticipated_monetary_total_id,
    order_line_id
):
    order = Order(
        id=id,
        ubl_version_id=ubl_version_id,
        customization_id=customization_id,
        profile_id=profile_id,
        sales_order_id=sales_order_id,
        copy_indicator=copy_indicator,
        uuid=uuid,
        issue_date=issue_date,
        note=note,
        buyer_customer_party_id=buyer_customer_party_id,
        seller_supplier_party_id=seller_supplier_party_id,
        originator_customer_party_id=originator_customer_party_id,
        delivery_id=delivery_id,
        delivery_terms_id=delivery_terms_id,
        transaction_conditions_id=transaction_conditions_id,
        anticipated_monetary_total_id=anticipated_monetary_total_id,
        order_line_id=order_line_id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session):
    return db.query(Order).all()

def update_order(
    db: Session,
    order_id: str,
    ubl_version_id: str = None,
    customization_id: str = None,
    profile_id: str = None,
    sales_order_id: str = None,
    copy_indicator: bool = None,
    uuid: str = None,
    issue_date: date = None,
    note: str = None,
    buyer_customer_party_id: int = None,
    seller_supplier_party_id: int = None,
    originator_customer_party_id: int = None,
    delivery_id: int = None,
    delivery_terms_id: int = None,
    transaction_conditions_id: int = None,
    anticipated_monetary_total_id: int = None,
    order_line_id: int = None
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return None

    if ubl_version_id: order.ubl_version_id = ubl_version_id
    if customization_id: order.customization_id = customization_id
    if profile_id: order.profile_id = profile_id
    if sales_order_id: order.sales_order_id = sales_order_id
    if copy_indicator is not None: order.copy_indicator = copy_indicator
    if uuid: order.uuid = uuid
    if issue_date: order.issue_date = issue_date
    if note: order.note = note
    if buyer_customer_party_id: order.buyer_customer_party_id = buyer_customer_party_id
    if seller_supplier_party_id: order.seller_supplier_party_id = seller_supplier_party_id
    if originator_customer_party_id: order.originator_customer_party_id = originator_customer_party_id
    if delivery_id: order.delivery_id = delivery_id
    if delivery_terms_id: order.delivery_terms_id = delivery_terms_id
    if transaction_conditions_id: order.transaction_conditions_id = transaction_conditions_id
    if anticipated_monetary_total_id: order.anticipated_monetary_total_id = anticipated_monetary_total_id
    if order_line_id: order.order_line_id = order_line_id

    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return order
