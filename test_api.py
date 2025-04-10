from datetime import date
import uuid
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app

# -------------------------------
# Test: GET /orders returns list of orders
# -------------------------------
def test_get_all_orders():
    with TestClient(app) as client:
        response = client.get("/orders")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0  # Should return at least one mock order

# -------------------------------
# Test: GET /orders contains a known mock order
# -------------------------------
def test_get_orders_contains_known_order():
    with TestClient(app) as client:
        response = client.get("/orders")
        assert response.status_code == 200
        orders = response.json()
        assert any(order["id"] == 1 for order in orders)  # Confirm mock order with ID 1 exists

# -------------------------------
# Test: GET /order/{id} for known existing order
# -------------------------------
def test_get_order_valid():
    with TestClient(app) as client:
        order_id = 1
        response = client.get(f"/order/{order_id}")
        assert response.status_code == 200
        assert "id" in response.json()

#  -------------------------------
# Test: DELETE /despatch-advice/{id} twice 
# -------------------------------
def test_delete_existing_despatch_advice():
    """Test deleting an existing order (despatch advice)"""
    with TestClient(app) as client:
        order_id = 1
        #currently 3 ids in database
        response = client.delete(f"/despatch-advice/{order_id}")
        assert response.status_code == 204

        response = client.delete(f"/despatch-advice/{order_id}")
        #alr deleted so should fail
        assert response.status_code == 404
        assert response.json() == {"detail": "Despatch advice not found"}

# -------------------------------
# Test: DELETE and GET consistency for same order
# -------------------------------
def test_delete_and_get():
    with TestClient(app) as client:
        order_id = 1
        #currently 3 ids in database
        response = client.delete(f"/despatch-advice/{order_id}")
        assert response.status_code == 204

        response = client.get(f"/order/{order_id}")
        assert response.status_code == 404

# -------------------------------
# Test: POST /despatch-advice/{id} with valid payload returns XML
# -------------------------------        
import xml.etree.ElementTree as ET
from fastapi.testclient import TestClient

def test_post_despadvice():
    with TestClient(app) as client:
        # Simulate creating the order if necessary
        order_id = 1  # Ensure this order exists in your mock data or database
        # Add any necessary pre-conditions or data insertion logic here

        response_data = {
            "note": "string",
            "despatch_advice_type": "string",
            "fulfillment": "string",
            "issue_date": "2025-04-09",
            "quantity": 0,
            "backorder": 0,
            "reason": "string"
        }
        response = client.post(f"/despatch-advice/{order_id}", json=response_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        assert response.status_code == 200
        assert b"<DespatchAdvice>" in response.content
        
        root = ET.fromstring(response.content)
        
        assert root.tag == "DespatchAdvice"
        
        assert root.find("id").text == "1"
        assert root.find("ubl_version_id").text == "2.1"
        assert root.find("customization_id").text == "standard"
        assert root.find("profile_id").text == "profile1"
        assert root.find("sales_order_id").text == "SO12345"
        assert root.find("copy_indicator").text == "false"
        assert root.find("uuid").text == "123e4567-e89b-12d3-a456-426614174000"
        assert root.find("issue_date").text == "2025-04-09"
        assert root.find("note").text == "Please process urgently."
        assert root.find("buyer_customer_party_id").text == "1"
        assert root.find("seller_supplier_party_id").text == "2"
        assert root.find("originator_customer_party_id").text == "3"
        assert root.find("delivery_id").text == "4"
        assert root.find("delivery_terms_id").text == "5"
        assert root.find("transaction_conditions_id").text == "6"
        assert root.find("anticipated_monetary_total_id").text == "7"
        assert root.find("order_line_id").text == "8"
        assert root.find("order_line/note").text == "string"
        assert root.find("despatch_advice_type").text == "string"
        assert root.find("fulfillment").text == "string"
        assert root.find("quantity").text == "0"
        assert root.find("backorder").text == "0"
        assert root.find("reason").text == "string"

# -------------------------------
# Test: Accessing a non-existent API route
# -------------------------------
def test_invalid_route_access():
    with TestClient(app) as client:
        response = client.get("/not-a-real-endpoint")
        assert response.status_code == 404

# -------------------------------
# Test: Method Not Allowed for GET-only route
# -------------------------------
def test_invalid_method_on_get_route():
    with TestClient(app) as client:
        response = client.post("/orders")
        assert response.status_code == 405  # Method Not Allowed

# -------------------------------
# Test: Multiple GET /orders calls return same number of orders
# -------------------------------
def test_repeated_get_orders_consistency():
    with TestClient(app) as client:
        response1 = client.get("/orders")
        response2 = client.get("/orders")
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert len(response1.json()) == len(response2.json())

# -------------------------------
# Test: GET /orders returns list of orders with expected fields
# -------------------------------
def test_get_orders_structure():
    with TestClient(app) as client:
        response = client.get("/orders")
        assert response.status_code == 200
        orders = response.json()
        assert isinstance(orders, list)
        if orders:
            assert "id" in orders[0]
            assert "sales_order_id" in orders[0]

# -------------------------------
# Test: POST /despatch-advice/{id} with quantity = 0
# -------------------------------
def test_post_despatch_advice_zero_quantity():
    with TestClient(app) as client:
        payload = {
            "note": "Zero quantity test",
            "despatch_advice_type": "Standard",
            "fulfillment": "None",
            "issue_date": "2025-04-10",
            "quantity": 0,
            "backorder": True,
            "reason": "Out of stock"
        }
        response = client.post("/despatch-advice/1", json=payload)
        assert response.status_code in [200]  

# -------------------------------
# Test: POST /despatch-advice/{id} after deleting orders 2 & 3
# -------------------------------
def test_post_despatch_advice_after_multiple_deletes():
    with TestClient(app) as client:
        for order_id in [2, 3]:
            # Step 1: Delete existing despatch advice
            del_response = client.delete(f"/despatch-advice/{order_id}")
            assert del_response.status_code == 204

            # Step 2: Try to create despatch advice again
            payload = {
                "note": f"Reposting for ID {order_id}",
                "despatch_advice_type": "Standard",
                "fulfillment": "Full",
                "issue_date": "2025-04-10",
                "quantity": 5,
                "backorder": False,
                "reason": "Retry"
            }
            post_response = client.post(f"/despatch-advice/{order_id}", json=payload)
            assert post_response.status_code == 404
            assert post_response.json()["detail"] == "Order not found"

