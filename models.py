from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date, time

# Models for the UBL Order

class Contact(BaseModel):
    name: str
    telephone: str
    telefax: str
    email: str


class TaxScheme(BaseModel):
    id: str
    tax_type_code: str


class PartyTaxScheme(BaseModel):
    registration_name: str
    company_id: str
    exemption_reason: Optional[str] = None
    tax_scheme: TaxScheme


class Address(BaseModel):
    street_name: str
    building_name: str
    building_number: str
    city_name: str
    postal_zone: str
    country_subentity: str
    address_line: str
    country_code: str


class Party(BaseModel):
    name: str
    postal_address: Address
    tax_scheme: PartyTaxScheme
    contact: Contact


class BuyerCustomerParty(BaseModel):
    customer_assigned_account_id: str
    supplier_assigned_account_id: str
    party: Party


class SellerSupplierParty(BaseModel):
    customer_assigned_account_id: str
    party: Party


class OriginatorCustomerParty(BaseModel):
    party: Party


class DeliveryPeriod(BaseModel):
    requested_delivery_start_date: date
    requested_delivery_start_time: time
    requested_delivery_end_date: date
    requested_delivery_end_time: time


class Delivery(BaseModel):
    delivery_address: Address
    delivery_period: DeliveryPeriod


class AnticipatedMonetaryTotal(BaseModel):
    currency_id: str
    line_extension_amount: float
    payable_amount: float


class TransactionConditions(BaseModel):
    description: str


class DeliveryTerms(BaseModel):
    special_terms: str


class Price(BaseModel):
    currency_id: str
    price_amount: float
    unit_code: str
    base_quantity: float
    

class ItemIdentification(BaseModel):
    id: str

class ItemInstance(BaseModel):
    lot_number_id: int
    expiry_date: date

class Item(BaseModel):
    description: str
    name: str
    buyers_item_identification: ItemIdentification
    sellers_item_identification: ItemIdentification
    item_instance: Optional[ItemInstance]


class LineItem(BaseModel):
    id: str
    sales_order_id: str
    line_status_code: str
    unit_code: str
    quantity: float
    currency_id: str
    line_extension_amount: float
    total_tax_amount: float
    price: Price
    item: Item


class OrderLine(BaseModel):
    note: Optional[str] = None
    line_item: LineItem


class Order(BaseModel):
    ubl_version_id: str
    customization_id: str
    profile_id: str
    id: str
    sales_order_id: str
    copy_indicator: bool
    uuid: str
    issue_date: date
    note: Optional[str] = None
    buyer_customer_party: BuyerCustomerParty
    seller_supplier_party: SellerSupplierParty
    originator_customer_party: OriginatorCustomerParty
    delivery: Delivery
    delivery_terms: DeliveryTerms
    transaction_conditions: TransactionConditions
    anticipated_monetary_total: AnticipatedMonetaryTotal
    order_line: OrderLine


# Models for the UBL Despatch Advice

class OrderReference(BaseModel):
    id: str
    sales_order_id: str
    uuid: str
    issue_date: date

class OrderLineReference(BaseModel):
    line_id: int
    sales_order_line_id: str
    order_reference: OrderReference

class DespatchLine(BaseModel):
    id: int
    note: Optional[str] = None
    line_status_code: str
    unit_code: str
    delivered_quantity: float
    backorder_quantity: float
    backorder_reason: str
    order_line_reference: OrderLineReference
    item: Item


class Shipment(BaseModel):
    id: int
    consignment_id: int
    delivery: Delivery


class DespatchAdvice(BaseModel):
    ubl_version_id: str
    customization_id: str
    profile_id: str
    id: str
    sales_order_id: str
    copy_indicator: bool
    uuid: str
    document_status_code: str
    despatch_advice_type_code: str
    note: Optional[str] = None
    order_reference: Order
    despatch_supplier_party: BuyerCustomerParty
    shipment: Shipment
    despatch_line: DespatchLine