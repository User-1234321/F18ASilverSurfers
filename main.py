from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI
# from f18asilversurfers.add_mock import add_mock_order_to_db
import uvicorn
from database import init_db, SessionLocal
from database import engine, SessionLocal
from models import order_models
from routes import order



order_models.Base.metadata.create_all(bind=engine)
mock_orders = [
    {'name': 'david', 'purchase': 'big cork'},
    {'name': 'richard', 'purchase': 'horse'},
    {'name': 'davsickyid', 'purchase': 'steak'},
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code will run when the app starts
    db: Session = SessionLocal()
    try:
        # Insert mock orders into the database
        for order in mock_orders:
            print("Starting app, inserting mock data")

            db.add(order_models.Order(**order))  # Add the mock orders to the session
        db.commit()  # Commit changes to the database
        yield  # The app will run here
    finally:
        # This code will run when the app shuts down
        db.query(order_models.Order).delete()  # Clean up the orders
        db.commit()  # Commit changes to remove all orders
        db.close()  # Close the session


app = FastAPI(lifespan=lifespan)

app.include_router(order.router)


# Run the app with uvicorn if this file is run directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
