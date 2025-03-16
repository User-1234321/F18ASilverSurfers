from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Order structure
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

class DespatchAdvice(BaseModel):
    note: str
    despatch_advice_type: str  
    fulfillment: str  
    issue_date: str 
    quantity: int
    backorder: Optional[str] = None
    reason: str

MOCK_ORDERS = {
    1: Order(
        order_id=1,
        buyer=BuyerSellerInfo(
            id="B12345",
            postal_address=PostalAddress(
                street_name="Elm Street",
                building_number="42A",
                city_name="Gotham",
                postal_zone="12345",
                country_sub_entity="NY",
                address_line="Apt 3B",
                country="USA"
            ),
            contact=ContactInfo(
                name="John Doe",
                telephone="123-456-7890",
                email="john@example.com"
            ),
            tax=TaxInfo(
                reg_name="John Doe Inc.",
                vat_gst_eori_tin_number="VAT123456",
                exemption_reason="N/A",
                tax_scheme="Standard"
            )
        ),
        seller=BuyerSellerInfo(
            id="S98765",
            postal_address=PostalAddress(
                street_name="Maple Avenue",
                building_number="99",
                city_name="Metropolis",
                postal_zone="54321",
                country_sub_entity="CA",
                address_line="Suite 10",
                country="USA"
            ),
            contact=ContactInfo(
                name="Jane Smith",
                telephone="987-654-3210",
                email="jane@seller.com"
            ),
            tax=TaxInfo(
                reg_name="Seller Corp.",
                vat_gst_eori_tin_number="VAT654321",
                exemption_reason=None,
                tax_scheme="Standard"
            )
        ),
        delivery=DeliveryInfo(
            postal_address=PostalAddress(
                street_name="Pine Street",
                building_number="21B",
                city_name="Star City",
                postal_zone="67890",
                country_sub_entity="TX",
                address_line="Warehouse 5",
                country="USA"
            ),
            start_date="2025-03-16",
            start_time="08:00",
            end_date="2025-03-17",
            end_time="18:00"
        ),
        delivery_terms="No deduction for late delivery",
        transaction_conditions="Payment within 30 days",
        transaction_method="Credit Card",
        total_owed=1500.75,
        order_line=OrderLine(
            id=1,
            sales_orders="SO123456",
            line_status_code="Confirmed",
            quantity_unit=1,
            line_extension_amount=1500,
            total_tax_amount=100,
            price=1500,
            description="High-end gaming laptop",
            name="Laptop Pro X",
            buyers_item_id="B-LAP-001",
            sellers_item_id="S-LAP-999"
        )
    )
}

@app.get("/orders")
def get_all_orders():
    """Fetch all mock orders."""
    return list(MOCK_ORDERS.values())

@app.get("/order/{order_id}")
def get_order(order_id: int):
    """Fetch a single mock order by ID."""
    order = MOCK_ORDERS.get(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.post("/despatch-advice/{order_id}")
def post_despatch_advice(order_id: int, advice: DespatchAdvice):
    """Post despatch advice for an order."""
    order = MOCK_ORDERS.get(order_id)
    if order:

        order_dict = order.dict()
        order_dict["order_line"]["note"] = advice.note
        order_dict["despatch_advice_type"] = advice.despatch_advice_type
        order_dict["fulfillment"] = advice.fulfillment
        order_dict["issue_date"] = advice.issue_date
        order_dict["quantity"] = advice.quantity
        order_dict["backorder"] = advice.backorder
        order_dict["reason"] = advice.reason
        return order_dict
    raise HTTPException(status_code=404, detail="Order not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
