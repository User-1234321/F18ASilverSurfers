from fastapi import FastAPI
from f18asilversurfers.add_mock import add_mock_order_to_db
import uvicorn

app = FastAPI(
    lifespan=lambda app: add_mock_order_to_db()  # Add mock order during startup
)

# Include your routers
from f18asilversurfers.routes import order, despatch_advice
app.include_router(order.router)
app.include_router(despatch_advice.router)

# Run the app with uvicorn if this file is run directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
