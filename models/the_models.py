# app/models.py
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid
from datetime import date

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    ubl_version_id = Column(String)
    customization_id = Column(String)
    profile_id = Column(String)
    sales_order_id = Column(String, unique=True)
    copy_indicator = Column(Boolean)
    uuid = Column(UUID, default=uuid.uuid4)
    issue_date = Column(Date, default=date.today)
    note = Column(String)
    buyer_customer_party_id = Column(Integer)
    seller_supplier_party_id = Column(Integer)
    originator_customer_party_id = Column(Integer)
    delivery_id = Column(Integer)
    delivery_terms_id = Column(Integer)
    transaction_conditions_id = Column(Integer)
    anticipated_monetary_total_id = Column(Integer)
    order_line_id = Column(Integer)

class DespatchAdviceDB(Base):
    __tablename__ = "despatch_advice"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String)
    despatch_advice_type = Column(String)
    fulfillment = Column(String)
    issue_date = Column(Date)
    quantity = Column(Integer)
    backorder = Column(Integer, nullable=True)
    reason = Column(String, nullable=True)