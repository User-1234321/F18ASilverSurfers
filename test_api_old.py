# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# # --------------------------
# # Test: GET all orders
# # --------------------------
# def test_get_all_orders():
#     response = client.get("/orders")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert len(response.json()) > 0  # Should return at least one mock order

# # --------------------------
# # Test: GET specific order (valid ID)
# # --------------------------
# def test_get_order_valid():
#     response = client.get("/order/1")
#     assert response.status_code == 200
#     assert "order_id" in response.json()

# # --------------------------
# # Test: GET specific order (invalid ID)
# # --------------------------
# def test_get_order_invalid():
#     response = client.get("/order/9999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Order not found"

# # --------------------------
# # Test: POST despatch advice (valid)
# # --------------------------
# def test_post_despatch_advice_valid():
#     advice_payload = {
#         "note": "Handle with care",
#         "despatch_advice_type": "Standard",
#         "fulfillment": "Complete",
#         "issue_date": "2025-04-01",
#         "quantity": 10,
#         "backorder": "None",
#         "reason": "Ready for shipment"
#     }
#     response = client.post("/despatch-advice/1", json=advice_payload)
#     assert response.status_code == 200
#     assert b"<DespatchAdvice>" in response.content  # XML root tag

# # --------------------------
# # Test: POST despatch advice (invalid order ID)
# # --------------------------
# def test_post_despatch_advice_invalid_order():
#     advice_payload = {
#         "note": "Invalid order test",
#         "despatch_advice_type": "Standard",
#         "fulfillment": "Partial",
#         "issue_date": "2025-04-01",
#         "quantity": 5,
#         "backorder": "Yes",
#         "reason": "Awaiting stock"
#     }
#     response = client.post("/despatch-advice/9999", json=advice_payload)
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Order not found"
