# test_crud.py
# Purpose: Unit tests for CRUD operations interacting with the Order model in the database.

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from database import Base, SessionLocal
from models.models import Order
from crud import create_order, get_orders, update_order, delete_order
from datetime import date

# Setup test database
TEST_DB_URL = "sqlite:///./test_crud.db"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Recreate DB schema
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    yield db
    db.close()

# Test 1: Ensure the "order" table exists after setup
def test_database_initialization():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "order" in tables

# Test 2: Create a new order in the database
def test_create_order(db):
    order = create_order(
        db,
        id="ORD001",
        ubl_version_id="2.1",
        customization_id="custom",
        profile_id="profile",
        sales_order_id="SO001",
        copy_indicator=False,
        uuid="uuid-001",
        issue_date=date(2025, 4, 1),
        note="Test Order",
        buyer_customer_party_id=1,
        seller_supplier_party_id=1,
        originator_customer_party_id=1,
        delivery_id=1,
        delivery_terms_id=1,
        transaction_conditions_id=1,
        anticipated_monetary_total_id=1,
        order_line_id=1,
    )
    assert order.id == "ORD001"

# Test 3: Retrieve all orders and ensure the list is not empty
def test_get_orders_not_empty(db):
    orders = get_orders(db)
    assert len(orders) > 0

# Test 4: Update the note field of an existing order
def test_update_order_note(db):
    updated = update_order(db, "ORD001", note="Updated Note")
    assert updated.note == "Updated Note"

# Test 5: Update multiple fields of the order
def test_update_order_multiple_fields(db):
    updated = update_order(db, "ORD001", sales_order_id="SO999", uuid="uuid-999")
    assert updated.sales_order_id == "SO999"
    assert updated.uuid == "uuid-999"

# Test 6: Try to delete a non-existent order
def test_delete_nonexistent_order(db):
    deleted = delete_order(db, "ORD-DOES-NOT-EXIST")
    assert deleted is None

# Test 7: Delete an existing order
def test_delete_order(db):
    deleted = delete_order(db, "ORD001")
    assert deleted.id == "ORD001"

# Test 8: Ensure all orders are deleted
def test_all_orders_deleted(db):
    assert get_orders(db) == []

# Test 9: Recreate another order for testing
def test_recreate_order_for_count(db):
    order = create_order(
        db,
        id="ORD002",
        ubl_version_id="2.1",
        customization_id="custom-2",
        profile_id="profile-2",
        sales_order_id="SO002",
        copy_indicator=True,
        uuid="uuid-002",
        issue_date=date(2025, 4, 2),
        note="Second Order",
        buyer_customer_party_id=2,
        seller_supplier_party_id=2,
        originator_customer_party_id=2,
        delivery_id=2,
        delivery_terms_id=2,
        transaction_conditions_id=2,
        anticipated_monetary_total_id=2,
        order_line_id=2,
    )
    assert order.id == "ORD002"

# Test 10: Ensure the recreated order exists
def test_check_recreated_order(db):
    orders = get_orders(db)
    assert any(order.id == "ORD002" for order in orders)
