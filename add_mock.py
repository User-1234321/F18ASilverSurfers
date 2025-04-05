from sqlalchemy.orm import Session
from f18asilversurfers.models.order_models import Order, BuyerSellerInfo, PostalAddress, ContactInfo, TaxInfo, DeliveryInfo, OrderLine
from f18asilversurfers.database import SessionLocal

def add_mock_order_to_db():
    db: Session = SessionLocal()
    # Check if mock data already exists
    if db.query(Order).count() == 0:  # If there are no orders in the database
        # Create mock data
        order = Order(
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
        db.add(order)
        db.commit()
        db.refresh(order)
    db.close()
