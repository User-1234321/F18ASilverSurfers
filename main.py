from contextlib import asynccontextmanager
from datetime import date
import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from f18asilversurfers.add_mock import add_mock_order_to_db
import uvicorn
from database import init_db, SessionLocal
from database import engine, SessionLocal
from models import the_models
from routes import order, despatch_advice
import os

from routes import despatch



# Drop and recreate the table to fix any schema issues
the_models.Base.metadata.drop_all(bind=engine)
the_models.Base.metadata.create_all(bind=engine)
mock_orders = [
    {
        'id': 1,
        'ubl_version_id': '2.1',
        'customization_id': 'standard',
        'profile_id': 'profile1',
        'sales_order_id': 'SO12345',
        'copy_indicator': False,
        'uuid': uuid.UUID('123e4567-e89b-12d3-a456-426614174000'),  # Convert string to UUID
        'issue_date': date(2025, 4, 6),
        'note': 'Please process urgently.',
        'buyer_customer_party_id': 1,
        'seller_supplier_party_id': 2,
        'originator_customer_party_id': 3,
        'delivery_id': 4,
        'delivery_terms_id': 5,
        'transaction_conditions_id': 6,
        'anticipated_monetary_total_id': 7,
        'order_line_id': 8
    },
    {
        'id': 2,
        'ubl_version_id': '2.1',
        'customization_id': 'standard',
        'profile_id': 'profile2',
        'sales_order_id': 'SO12346',
        'copy_indicator': False,
        'uuid': uuid.UUID('123e4567-e89b-12d3-a456-426614174001'),  # Convert string to UUID
        'issue_date': date(2025, 4, 6),
        'note': 'Include the special packaging.',
        'buyer_customer_party_id': 9,
        'seller_supplier_party_id': 10,
        'originator_customer_party_id': 11,
        'delivery_id': 12,
        'delivery_terms_id': 13,
        'transaction_conditions_id': 14,
        'anticipated_monetary_total_id': 15,
        'order_line_id': 16
    },
    {
        'id': 3,
        'ubl_version_id': '2.1',
        'customization_id': 'standard',
        'profile_id': 'profile3',
        'sales_order_id': 'SO12347',
        'copy_indicator': True,
        'uuid': uuid.UUID('123e4567-e89b-12d3-a456-426614174002'),  # Convert string to UUID
        'issue_date': date(2025, 4, 6),
        'note': 'Urgent delivery required.',
        'buyer_customer_party_id': 17,
        'seller_supplier_party_id': 18,
        'originator_customer_party_id': 19,
        'delivery_id': 20,
        'delivery_terms_id': 21,
        'transaction_conditions_id': 22,
        'anticipated_monetary_total_id': 23,
        'order_line_id': 24
    }
]

#mock_despatch_advices = [
#    {
#        'id': 1,
#        'note': 'Urgent despatch needed.',
#        'despatch_advice_type': 'Standard',
#        'fulfillment': 'Complete',
#        'issue_date': date(2025, 4, 6),
#        'quantity': 100,
#        'backorder': None,
#        'reason': 'Customer request'
#    },
#    {
#        'id': 2,
#        'note': 'Express despatch for VIP customer.',
#        'despatch_advice_type': 'Express',
#        'fulfillment': 'Partial',
#        'issue_date': date(2025, 4, 6),
#        'quantity': 50,
#        'backorder': 25,
#        'reason': 'VIP Priority'
#    }
#]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code will run when the app starts
    db: Session = SessionLocal()
    try:
        # Insert mock orders into the database
        for order in mock_orders:
            print("Starting app, inserting mock data")

            db.add(the_models.Order(**order))  # Add the mock orders to the session

        #for despatch_advice in mock_despatch_advices:
            #print("Starting app, inserting mock despatch advice data")
            #db.add(the_models.DespatchAdviceDB(**despatch_advice))
            ##adds mock despatch into databse for access
        db.commit()  # Commit changes to the database
        yield  # The app will run here
    finally:
        # This code will run when the app shuts down
        db.query(the_models.Order).delete()  # Clean up the orders
        db.commit()  # Commit changes to remove all orders
        db.close()  # Close the session


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order.router)
app.include_router(despatch_advice.router)

app.include_router(despatch.router)



# Run the app with uvicorn if this file is run directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # fallback to 10000 locally
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
