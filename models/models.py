from sqlalchemy import Column, String, Integer, Float, Boolean, Date, Time, ForeignKey, Text, Numeric, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    telefax = Column(String, nullable=False)
    email = Column(String, nullable=False)

class TaxScheme(Base):
    __tablename__ = "tax_scheme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tax_type_code = Column(String, nullable=False)

class PartyTaxScheme(Base):
    __tablename__ = "party_tax_scheme"
    id = Column(Integer, primary_key=True, autoincrement=True)
    registration_name = Column(String, nullable=False)
    company_id = Column(String, nullable=False)
    exemption_reason = Column(String, nullable=False)
    tax_scheme_id = Column(Integer, ForeignKey("tax_scheme.id"), nullable=False)
    tax_scheme = relationship("TaxScheme")

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    street_name = Column(String, nullable=False)
    building_name = Column(String, nullable=False)
    building_number = Column(String, nullable=False)
    city_name = Column(String, nullable=False)
    postal_zone = Column(String, nullable=False)
    country_subentity = Column(String, nullable=False)
    address_line = Column(String, nullable=False)
    country_code = Column(String, nullable=False)

class Party(Base):
    __tablename__ = "party"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    postal_address_id = Column(Integer, ForeignKey("address.id"), nullable=False)
    tax_scheme_id = Column(Integer, ForeignKey("party_tax_scheme.id"), nullable=False)
    contact_id = Column(Integer, ForeignKey("contact.id"), nullable=False)
    postal_address = relationship("Address")
    tax_scheme = relationship("PartyTaxScheme")
    contact = relationship("Contact")

class BuyerCustomerParty(Base):
    __tablename__ = 'buyer_customer_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_assigned_account_id = Column(String, nullable=False)
    supplier_assigned_account_id = Column(String, nullable=False)
    party_id = Column(Integer, ForeignKey('party.id'), nullable=False)
    party = relationship('Party')

class SellerSupplierParty(Base):
    __tablename__ = 'seller_supplier_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_assigned_account_id = Column(String, nullable=False)
    party_id = Column(Integer, ForeignKey('party.id'), nullable=False)
    party = relationship('Party')    

class OriginatorCustomerParty(Base):
    __tablename__ = 'originator_customer_party'
    id = Column(Integer, primary_key=True, autoincrement=True)
    party_id = Column(Integer, ForeignKey('party.id'), nullable=False)
    party = relationship('Party')  

class DeliveryPeriod(Base):
    __tablename__ = 'delivery_period'
    id = Column(Integer, primary_key=True, autoincrement=True)
    requested_delivery_start_date = Column(Date, nullable=False)
    requested_delivery_start_time = Column(Time, nullable=False)
    requested_delivery_end_date = Column(Date, nullable=False)
    requested_delivery_end_time = Column(Time, nullable=False)

class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    delivery_period_id = Column(Integer, ForeignKey('delivery_period.id'), nullable=False)
    delivery_address = relationship('Address')
    delivery_period = relationship('DeliveryPeriod')

class AnticipatedMonetaryTotal(Base):
    __tablename__ = 'anticipated_monetary_total'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id = Column(String, nullable=False)
    line_extension_amount = Column(Numeric(18, 2), nullable=False)
    payable_amount = Column(Numeric(18, 2), nullable=False)

class TransactionConditions(Base):
    __tablename__ = 'transaction_conditions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)

class DeliveryTerms(Base):
    __tablename__ = 'delivery_terms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    special_terms = Column(String, nullable=False)

class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id = Column(String, nullable=False)
    price_amount = Column(Numeric(18, 2), nullable=False)
    unit_code = Column(String, nullable=False)
    base_quantity = Column(Float, nullable=False)

class ItemIdentification(Base):
    __tablename__ = 'item_identification'
    id = Column(String, primary_key=True, nullable=False)

class ItemInstance(Base):
    __tablename__ = 'item_instance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lot_number_id = Column(Integer, nullable=False)
    expiry_date = Column(Date, nullable=False)

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    name = Column(String, nullable=False)
    buyers_item_identification_id = Column(String, ForeignKey('item_identification.id'), nullable=False)
    sellers_item_identification_id = Column(String, ForeignKey('item_identification.id'), nullable=False)
    item_instance_id = Column(Integer, ForeignKey('item_instance.id'), nullable=False)
    buyers_item_identification = relationship('ItemIdentification', foreign_keys=[buyers_item_identification_id])
    sellers_item_identification = relationship('ItemIdentification', foreign_keys=[sellers_item_identification_id])
    item_instance = relationship('ItemInstance')

class LineItem(Base):
    __tablename__ = 'line_item'
    id = Column(String, primary_key=True, nullable=False)
    sales_order_id = Column(String, nullable=False)
    line_status_code = Column(String, nullable=False)
    unit_code = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    currency_id = Column(String, nullable=False)
    line_extension_amount = Column(Numeric(18, 2), nullable=False)
    total_tax_amount = Column(Numeric(18, 2), nullable=False)
    price_id = Column(Integer, ForeignKey('price.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    price = relationship('Price')
    item = relationship('Item')

class OrderLine(Base):
    __tablename__ = 'order_line'
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(Text, nullable=False)
    line_item_id = Column(String, ForeignKey('line_item.id'), nullable=False)
    line_item = relationship('LineItem')  

class Order(Base):
    __tablename__ = 'order'
    id = Column(String, primary_key=True, nullable=False)
    ubl_version_id = Column(String, nullable=False)
    customization_id = Column(String, nullable=False)
    profile_id = Column(String, nullable=False)
    sales_order_id = Column(String, nullable=False)
    copy_indicator = Column(Boolean, nullable=False)
    uuid = Column(String, nullable=False)
    issue_date = Column(Date, nullable=False)
    note = Column(Text, nullable=False)
    buyer_customer_party_id = Column(Integer, ForeignKey('buyer_customer_party.id'), nullable=False)
    seller_supplier_party_id = Column(Integer, ForeignKey('seller_supplier_party.id'), nullable=False)
    originator_customer_party_id = Column(Integer, ForeignKey('originator_customer_party.id'), nullable=False)
    delivery_id = Column(Integer, ForeignKey('delivery.id'), nullable=False)
    delivery_terms_id = Column(Integer, ForeignKey('delivery_terms.id'), nullable=False)
    transaction_conditions_id = Column(Integer, ForeignKey('transaction_conditions.id'), nullable=False)
    anticipated_monetary_total_id = Column(Integer, ForeignKey('anticipated_monetary_total.id'), nullable=False)
    order_line_id = Column(Integer, ForeignKey('order_line.id'), nullable=False)
    
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
    id = Column(String, primary_key=True, nullable=False)
    sales_order_id = Column(String, nullable=False)
    uuid = Column(String, nullable=False)
    issue_date = Column(Date, nullable=False)

class OrderLineReference(Base):
    __tablename__ = 'order_line_reference'
    id = Column(Integer, primary_key=True, autoincrement=True)
    line_id = Column(Integer, nullable=False)
    sales_order_line_id = Column(String, nullable=False)
    order_reference_id = Column(String, ForeignKey('order_reference.id'), nullable=False)
    order_reference = relationship('OrderReference')

class DespatchLine(Base):
    __tablename__ = 'despatch_line'
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(Text, nullable=False)
    line_status_code = Column(String, nullable=False)
    unit_code = Column(String, nullable=False)
    delivered_quantity = Column(Float, nullable=False)
    backorder_quantity = Column(Float, nullable=False)
    backorder_reason = Column(String, nullable=False)
    order_line_reference_id = Column(Integer, ForeignKey('order_line_reference.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    
    order_line_reference = relationship('OrderLineReference')
    item = relationship('Item')

class Shipment(Base):
    __tablename__ = 'shipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    consignment_id = Column(Integer, nullable=False)
    delivery_id = Column(Integer, ForeignKey('delivery.id'), nullable=False)
    delivery = relationship('Delivery')

class DespatchAdvice(Base):
    __tablename__ = 'despatch_advice'
    id = Column(String, primary_key=True, nullable=False)
    ubl_version_id = Column(String, nullable=False)
    customization_id = Column(String, nullable=False)
    profile_id = Column(String, nullable=False)
    sales_order_id = Column(String, nullable=False)
    copy_indicator = Column(Boolean, nullable=False)
    uuid = Column(String, nullable=False)
    document_status_code = Column(String, nullable=False)
    despatch_advice_type_code = Column(String, nullable=False)
    note = Column(Text, nullable=False)
    order_reference_id = Column(String, ForeignKey('order_reference.id'), nullable=False)
    despatch_supplier_party_id = Column(Integer, ForeignKey('buyer_customer_party.id'), nullable=False)
    shipment_id = Column(Integer, ForeignKey('shipment.id'), nullable=False)
    despatch_line_id = Column(Integer, ForeignKey('despatch_line.id'), nullable=False)
    
    order_reference = relationship('OrderReference')
    despatch_supplier_party = relationship('BuyerCustomerParty')
    shipment = relationship('Shipment')
    despatch_line = relationship('DespatchLine')

Base.metadata.create_all(bind=engine)
