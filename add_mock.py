# from sqlalchemy.orm import Session
# from f18asilversurfers.models.order_models import Order, BuyerSellerInfo, PostalAddress, ContactInfo, TaxInfo, DeliveryInfo, OrderLine
# from f18asilversurfers.database import SessionLocal
# from f18asilversurfers.data.mock_orders import MOCK_ORDERS

# def add_mock_order_to_db():
#     # Use the context manager for session handling
#     with SessionLocal() as db:
#         # Check if mock data already exists
#         if db.query(Order).count() == 0:  # If there are no orders in the database
#             # Create mock data
#             order = MOCK_ORDERS
#             db.add(order)
#             db.commit()
#             db.refresh(order)
