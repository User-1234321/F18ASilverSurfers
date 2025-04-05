from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped
from typing import Optional

Base = declarative_base()

class ContactInfo(Base):
    __tablename__ = 'contact_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    telephone: Mapped[str]
    email: Mapped[str]

class TaxInfo(Base):
    __tablename__ = 'tax_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_name: Mapped[str]
    vat_gst_eori_tin_number: Mapped[str]
    exemption_reason: Optional[Mapped[str]] = None  # Correctly using Optional with Mapped
    tax_scheme: Mapped[str]

class PostalAddress(Base):
    __tablename__ = 'postal_address'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    street_name: Mapped[str]
    building_number: Mapped[str]
    city_name: Mapped[str]
    postal_zone: Mapped[str]
    country_sub_entity: Mapped[str]
    address_line: Mapped[str]
    country: Mapped[str]

class BuyerSellerInfo(Base):
    __tablename__ = 'buyer_seller_info'
    
    id = Column(String, primary_key=True)
    postal_address: Mapped[PostalAddress]  # Correctly using Mapped for relationships
    contact: Mapped[ContactInfo]
    tax: Mapped[TaxInfo]

class DeliveryInfo(Base):
    __tablename__ = 'delivery_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    postal_address: Mapped[PostalAddress]
    start_date: Mapped[str]
    start_time: Mapped[str]
    end_date: Mapped[str]
    end_time: Mapped[str]

class OrderLine(Base):
    __tablename__ = 'order_line'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sales_orders: Mapped[str]
    line_status_code: Mapped[str]
    quantity_unit: Mapped[int]
    line_extension_amount: Mapped[int]
    total_tax_amount: Mapped[int]
    price: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    buyers_item_id: Mapped[str]
    sellers_item_id: Mapped[str]

class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True)
    buyer_id = Column(String, ForeignKey('buyer_seller_info.id'))
    seller_id = Column(String, ForeignKey('buyer_seller_info.id'))
    delivery_id = Column(Integer, ForeignKey('delivery_info.id'))
    
    buyer: Mapped[BuyerSellerInfo] = relationship("BuyerSellerInfo", foreign_keys=[buyer_id])
    seller: Mapped[BuyerSellerInfo] = relationship("BuyerSellerInfo", foreign_keys=[seller_id])
    delivery: Mapped[DeliveryInfo] = relationship("DeliveryInfo", back_populates="orders")
    order_lines: Mapped[list[OrderLine]] = relationship("OrderLine", back_populates="order")

# Ensure that your database models reflect this updated code structure.
