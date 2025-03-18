import pytest
from fastapi.testclient import TestClient
from uuid import UUID
from datetime import datetime
from app.main import app
from app.database import Base, engine
from app.models.product import Product

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

class TestProductValidation:
    def test_valid_product_creation(self, client):
        product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "category": "Test Category",
            "stock_quantity": 10
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == product_data["name"]
        assert data["price"] == product_data["price"]
        assert data["stock_quantity"] == product_data["stock_quantity"]
        assert UUID(data["id"])
        assert datetime.fromisoformat(data["created_at"].replace('Z', '+00:00'))

    def test_invalid_price(self, client):
        # Test negative price
        product_data = {
            "name": "Test Product",
            "price": -10.0,
            "category": "Test Category",
            "stock_quantity": 10
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 422

        # Test zero price
        product_data["price"] = 0
        response = client.post("/products/", json=product_data)
        assert response.status_code == 422

    def test_invalid_stock_quantity(self, client):
        # Test negative stock
        product_data = {
            "name": "Test Product",
            "price": 99.99,
            "category": "Test Category",
            "stock_quantity": -1
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 422

    def test_missing_required_fields(self, client):
        # Test missing name
        product_data = {
            "price": 99.99,
            "category": "Test Category",
            "stock_quantity": 10
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 422

        # Test missing category
        product_data = {
            "name": "Test Product",
            "price": 99.99,
            "stock_quantity": 10
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 422

    def test_optional_description(self, client):
        # Test with description
        product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "category": "Test Category",
            "stock_quantity": 10
        }
        response = client.post("/products/", json=product_data)
        assert response.status_code == 201
        assert response.json()["description"] == "Test Description"

        # Test without description
        product_data.pop("description")
        response = client.post("/products/", json=product_data)
        assert response.status_code == 201
        assert response.json()["description"] is None