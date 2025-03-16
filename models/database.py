from sqlalchemy import Column, String, Integer, Float, Boolean, Date, Time, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
# from enum import Enum as PyEnum

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    telephone = Column(String)
    telefax = Column(String)
    email = Column(String)

class TaxScheme(Base):
    __tablename__ = "tax_scheme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tax_type_code = Column(String)

class PartyTaxScheme(Base):
    __tablename__ = "party_tax_scheme"
    id = Column(Integer, primary_key=True, autoincrement=True)
    registration_name = Column(String)
    company_id = Column(String)
    exemption_reason = Column(String)
    tax_scheme_id = Column(Integer, ForeignKey("tax_scheme.id"))
    tax_scheme = relationship("TaxScheme")

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    street_name = Column(String)
    building_name = Column(String)
    building_number = Column(String)
    city_name = Column(String)
    postal_zone = Column(String)
    country_subentity = Column(String)
    address_line = Column(String)
    country_code = Column(String)

class Party(Base):
    __tablename__ = "party"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    postal_address_id = Column(Integer, ForeignKey("address.id"))
    tax_scheme_id = Column(Integer, ForeignKey("party_tax_scheme.id"))
    contact_id = Column(Integer, ForeignKey("contact.id"))
    postal_address = relationship("Address")
    tax_scheme = relationship("PartyTaxScheme")
    contact = relationship("Contact")

class BuyerCustomerParty(Base):
    __tablename__ = 'buyer_customer_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_assigned_account_id = Column(String)
    supplier_assigned_account_id = Column(String)
    party_id = Column(Integer, ForeignKey('party.id'))
    party = relationship('Party')

class SellerSupplierParty(Base):
    __tablename__ = 'seller_supplier_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_assigned_account_id = Column(String)
    party_id = Column(Integer, ForeignKey('party.id'))
    party = relationship('Party')    

class OriginatorCustomerParty(Base):
    __tablename__ = 'originator_customer_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    party_id = Column(Integer, ForeignKey('party.id'))
    party = relationship('Party')  

class DeliveryPeriod(Base):
    __tablename__ = 'delivery_period'
    id = Column(Integer, primary_key=True, autoincrement=True)
    requested_delivery_start_date = Column(Date)
    requested_delivery_start_time = Column(Time)
    requested_delivery_end_date = Column(Date)
    requested_delivery_end_time = Column(Time)

class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_address_id = Column(Integer, ForeignKey('address.id'))
    delivery_period_id = Column(Integer, ForeignKey('delivery_period.id'))
    delivery_address = relationship('Address')
    delivery_period = relationship('DeliveryPeriod')

class AnticipatedMonetaryTotal(Base):
    __tablename__ = 'anticipated_monetary_total'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id = Column(String)
    line_extension_amount = Column(Decimal)
    payable_amount = Column(Decimal)

class TransactionConditions(Base):
    __tablename__ = 'transaction_conditions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)

class DeliveryTerms(Base):
    __tablename__ = 'delivery_terms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    special_terms = Column(String)

class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id = Column(String)
    price_amount = Column(Decimal)
    unit_code = Column(String)
    base_quantity = Column(Float)

class ItemIdentification(Base):
    __tablename__ = 'item_identification'
    id = Column(String, primary_key=True)

class ItemInstance(Base):
    __tablename__ = 'item_instance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lot_number_id = Column(Integer)
    expiry_date = Column(Date)

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    name = Column(String)
    buyers_item_identification_id = Column(String, ForeignKey('item_identification.id'))
    sellers_item_identification_id = Column(String, ForeignKey('item_identification.id'))
    item_instance_id = Column(Integer, ForeignKey('item_instance.id'))
    buyers_item_identification = relationship('ItemIdentification', foreign_keys=[buyers_item_identification_id])
    sellers_item_identification = relationship('ItemIdentification', foreign_keys=[sellers_item_identification_id])
    item_instance = relationship('ItemInstance')

class LineItem(Base):
    __tablename__ = 'line_item'
    id = Column(String, primary_key=True)
    sales_order_id = Column(String)
    line_status_code = Column(String)
    unit_code = Column(String)
    quantity = Column(Float)
    currency_id = Column(String)
    line_extension_amount = Column(Decimal)
    total_tax_amount = Column(Decimal)
    price_id = Column(Integer, ForeignKey('price.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    price = relationship('Price')
    item = relationship('Item')

class OrderLine(Base):
    __tablename__ = 'order_line'
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(Text)
    line_item_id = Column(String, ForeignKey('line_item.id'))
    line_item = relationship('LineItem')  

class Order(Base):
    __tablename__ = 'order'
    id = Column(String, primary_key=True)
    ubl_version_id = Column(String)
    customization_id = Column(String)
    profile_id = Column(String)
    sales_order_id = Column(String)
    copy_indicator = Column(Boolean)
    uuid = Column(String)
    issue_date = Column(Date)
    note = Column(Text)
    buyer_customer_party_id = Column(Integer, ForeignKey('buyer_customer_party.id'))
    seller_supplier_party_id = Column(Integer, ForeignKey('seller_supplier_party.id'))
    originator_customer_party_id = Column(Integer, ForeignKey('originator_customer_party.id'))
    delivery_id = Column(Integer, ForeignKey('delivery.id'))
    delivery_terms_id = Column(Integer, ForeignKey('delivery_terms.id'))
    transaction_conditions_id = Column(Integer, ForeignKey('transaction_conditions.id'))
    anticipated_monetary_total_id = Column(Integer, ForeignKey('anticipated_monetary_total.id'))
    order_line_id = Column(Integer, ForeignKey('order_line.id'))
    
    buyer_customer_party = relationship('BuyerCustomerParty')
    seller_supplier_party = relationship('SellerSupplierParty')
    originator_customer_party = relationship('OriginatorCustomerParty')
    delivery = relationship('Delivery')
    delivery_terms = relationship('DeliveryTerms')
    transaction_conditions = relationship('TransactionConditions')
    anticipated_monetary_total = relationship('AnticipatedMonetaryTotal')
    order_line = relationship('OrderLine')

class OrderReference(Base):
    __tablename__ = 'order_reference'
    id = Column(String, primary_key=True)
    sales_order_id = Column(String)
    uuid = Column(String)
    issue_date = Column(Date)

class OrderLineReference(Base):
    __tablename__ = 'order_line_reference'
    id = Column(Integer, primary_key=True, autoincrement=True)
    line_id = Column(Integer)
    sales_order_line_id = Column(String)
    order_reference_id = Column(String, ForeignKey('order_reference.id'))
    order_reference = relationship('OrderReference')

class DespatchLine(Base):
    __tablename__ = 'despatch_line'
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(Text)
    line_status_code = Column(String)
    unit_code = Column(String)
    delivered_quantity = Column(Float)
    backorder_quantity = Column(Float)
    backorder_reason = Column(String)
    order_line_reference_id = Column(Integer, ForeignKey('order_line_reference.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    
    order_line_reference = relationship('OrderLineReference')
    item = relationship('Item')

class Shipment(Base):
    __tablename__ = 'shipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    consignment_id = Column(Integer)
    delivery_id = Column(Integer, ForeignKey('delivery.id'))
    delivery = relationship('Delivery')

class DespatchAdvice(Base):
    __tablename__ = 'despatch_advice'
    id = Column(String, primary_key=True)
    ubl_version_id = Column(String)
    customization_id = Column(String)
    profile_id = Column(String)
    sales_order_id = Column(String)
    copy_indicator = Column(Boolean)
    uuid = Column(String)
    document_status_code = Column(String)
    despatch_advice_type_code = Column(String)
    note = Column(Text)
    order_reference_id = Column(String, ForeignKey('order_reference.id'))
    despatch_supplier_party_id = Column(Integer, ForeignKey('buyer_customer_party.id'))
    shipment_id = Column(Integer, ForeignKey('shipment.id'))
    despatch_line_id = Column(Integer, ForeignKey('despatch_line.id'))
    
    order_reference = relationship('OrderReference')
    despatch_supplier_party = relationship('BuyerCustomerParty')
    shipment = relationship('Shipment')
    despatch_line = relationship('DespatchLine')



Base.metadata.create_all(bind=engine)
