import pytest
from products import Product


def test_create_normal_product():
    # Test creating a normal product
    product = Product(name="Laptop", price=1000, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.is_active() == True


def test_create_invalid_product():
    # Test creating a product with invalid details
    with pytest.raises(ValueError):
        Product(name="", price=1450, quantity=100)  # Empty name
    with pytest.raises(ValueError):
        Product(name="MacBook Air M2", price=-10, quantity=100)  # Negative Price


def test_inactive_product():
    # Test that when a product reaches 0 quantity, it becomes inactive
    product = Product(name="Phone", price=500, quantity=0)
    assert product.is_active() == False


def test_product_purchase():
    # Test that product purchase modifies the quantity and returns the right output
    product = Product(name="Table", price=50, quantity=10)
    total_price = product.buy(quantity=5)
    assert total_price == 250  # 5 * 50 = 250
    assert product.quantity == 5


def test_insufficient_quantity():
    # Test that buying a larger quantity than exists invokes exception
    product = Product(name="Chair", price=20, quantity=10)
    with pytest.raises(ValueError):
        product.buy(quantity=15)  # Buying more than available quantity
