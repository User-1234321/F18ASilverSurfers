from pydantic import BaseModel
from typing import Optional

class ContactInfo(BaseModel):
    name: str
    telephone: str
    email: str

class TaxInfo(BaseModel):
    reg_name: str
    vat_gst_eori_tin_number: str
    exemption_reason: Optional[str] = None
    tax_scheme: str

class PostalAddress(BaseModel):
    street_name: str
    building_number: str
    city_name: str
    postal_zone: str
    country_sub_entity: str
    address_line: str
    country: str

class BuyerSellerInfo(BaseModel):
    id: str
    postal_address: PostalAddress
    contact: ContactInfo
    tax: TaxInfo

class DeliveryInfo(BaseModel):
    postal_address: PostalAddress
    start_date: str
    start_time: str
    end_date: str
    end_time: str

class OrderLine(BaseModel):
    note: Optional[str] = None
    id: int
    sales_orders: str
    line_status_code: str
    quantity_unit: int
    line_extension_amount: int
    total_tax_amount: int
    price: int
    description: str
    name: str
    buyers_item_id: str
    sellers_item_id: str

class Order(BaseModel):
    order_id: int
    buyer: BuyerSellerInfo
    seller: BuyerSellerInfo
    delivery: DeliveryInfo
    delivery_terms: str
    transaction_conditions: str
    transaction_method: str
    total_owed: float
    order_line: OrderLine