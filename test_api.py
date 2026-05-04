import requests

def test_get_all_products():
    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200

def test_products_count():
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    assert len(products) == 20

def test_get_single_product():
    response = requests.get("https://fakestoreapi.com/products/1")
    product = response.json()
    
    assert response.status_code == 200
    assert product["id"] == 1
    assert "title" in product
    assert "price" in product

def test_product_price():
    response = requests.get("https://fakestoreapi.com/products/1")
    product = response.json()

    assert response.status_code == 200
    assert product["price"] > 0
    

import pytest

@pytest.mark.xfail(reason="Bug: API returns 200 for nonexistent product")
def test_nonexistent_product():
    response = requests.get("https://fakestoreapi.com/products/9999")
    assert response.status_code == 404