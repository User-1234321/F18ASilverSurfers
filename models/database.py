from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from enum import Enum as PyEnum

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DespatchType(PyEnum):
    DELIVERY = "Delivery"
    RETURN = "Return"
    CANCEL = "Cancel"

class FulfillmentType(PyEnum):
    FULL = "Full"
    PARTIAL = "Partial"

class DespatchAdviceDB(Base):
    __tablename__ = "despatch_advices"

    id = Column(Integer, primary_key=True, index=True)
    despatch_type = Column(Enum(DespatchType), index=True)
    fulfillment = Column(Enum(FulfillmentType))
    order_id = Column(Integer, ForeignKey("orders.order_id"))

    order = relationship("OrderDB", back_populates="despatch_advices")

class OrderDB(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer)
    buyer_address = Column(String)
    buyer_contact = Column(String)
    seller_id = Column(Integer)
    seller_address = Column(String)
    seller_contact = Column(String)
    delivery_address = Column(String)
    requested_delivery_period = Column(String)
    transaction_conditions = Column(String)

    despatch_advices = relationship("DespatchAdviceDB", back_populates="order")

Base.metadata.create_all(bind=engine)
