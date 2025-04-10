from fastapi.testclient import TestClient
from main import app

def test_despatch_advice_success_scenario():
    with TestClient(app) as client:  
        # Step 1: Confirm the mock order exists (ID = 1)
        response = client.get("/order/1")
        assert response.status_code == 200  # Must exist
        data = response.json()
        assert data["id"] == 1
        assert data["sales_order_id"] == "SO12345"

        # Step 2: GET /orders must succeed and contain the mock order
        response = client.get("/orders")
        assert response.status_code == 200
        assert any(order["id"] == 1 for order in response.json())

        # Step 3: POST /despatch-advice/1 with valid payload
        payload = {
            "note": "Packed and ready for delivery",
            "despatch_advice_type": "Standard",
            "fulfillment": "Full",
            "issue_date": "2025-04-06",
            "quantity": 100,
            "backorder": False,
            "reason": "All stock available"
        }
        response = client.post("/despatch-advice/1", json=payload)
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/xml"
        assert b"<DespatchAdvice>" in response.content

# -------------------------------
# Test: POST /despatch-advice/{order_id} with invalid data
# -------------------------------
def test_post_despatch_advice_invalid_cases():
    with TestClient(app) as client:
        # ❌ Case 1: Missing required fields
        payload = {}  # Empty body
        response = client.post("/despatch-advice/1", json=payload)
        assert response.status_code == 422  # Unprocessable Entity

        # ❌ Case 2: Invalid field types (e.g. string instead of expected types)
        payload = {
            "note": 123,  # should be a string
            "despatch_advice_type": True,  # should be a string
            "fulfillment": 456,  # should be a string
            "issue_date": "invalid-date",  # should be a valid ISO date
            "quantity": "lots",  # should be an int or float
            "backorder": "maybe",  # should be a boolean
            "reason": 999  # should be a string
        }
        response = client.post("/despatch-advice/1", json=payload)
        assert response.status_code == 422

        # ❌ Case 3: Non-existent order ID
        payload = {
            "note": "Anything",
            "despatch_advice_type": "Standard",
            "fulfillment": "Full",
            "issue_date": "2025-04-10",
            "quantity": 1,
            "backorder": False,
            "reason": "Test"
        }
        response = client.post("/despatch-advice/9999", json=payload)
        assert response.status_code == 404
        assert response.json()["detail"] == "Order not found"

# -------------------------------
# Test: Mixed valid and invalid API interactions
# -------------------------------
def test_despatch_advice_mixed_cases():
    with TestClient(app) as client:
        # ✅ Case 1: Valid POST to /despatch-advice/1
        valid_payload = {
            "note": "Pack with care",
            "despatch_advice_type": "Express",
            "fulfillment": "Partial",
            "issue_date": "2025-04-15",
            "quantity": 5,
            "backorder": True,
            "reason": "Some items delayed"
        }
        response = client.post("/despatch-advice/1", json=valid_payload)
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/xml"

        # ❌ Case 2: Non-existent order ID
        response = client.post("/despatch-advice/9999", json=valid_payload)
        assert response.status_code == 404
        assert response.json()["detail"] == "Order not found"

        # ❌ Case 3: Invalid route
        response = client.get("/despatch-advicez/1")  # typo in route
        assert response.status_code == 404

        # ✅ Case 4: GET /orders should return list of orders
        response = client.get("/orders")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
