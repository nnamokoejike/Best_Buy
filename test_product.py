# test_products.py

import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_create_normal_product():
    """
    Test creating a normal product.
    """
    product = Product(name="Laptop", price=1000, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.is_active() is True


def test_create_non_stocked_product():
    """
    Test creating a non-stocked product.
    """
    product = NonStockedProduct(name="Software License", price=200)
    assert product.name == "Software License"
    assert product.price == 200
    assert product.quantity == 0
    assert product.is_active() is True


def test_create_limited_product():
    """
    Test creating a limited product.
    """
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1
    assert product.is_active() is True


def test_product_inactive():
    """
    Test that an inactive product has zero quantity.
    """
    product = Product(name="Phone", price=500, quantity=0)
    assert product.is_active() is False


def test_product_purchase():
    """
    Test product purchase functionality.
    """
    product = Product(name="Table", price=50, quantity=10)
    total_price = product.buy(quantity=5)
    assert total_price == 250  # 5 * 50 = 250
    assert product.quantity == 5


def test_insufficient_quantity():
    """
    Test that buying more than available quantity raises an exception.
    """
    product = Product(name="Chair", price=20, quantity=10)
    with pytest.raises(ValueError):
        product.buy(quantity=15)  # Buying more than available quantity


def test_percent_discount():
    """
    Test percentage discount promotion.
    """
    product = Product(name="Laptop", price=1000, quantity=10)
    promotion = PercentDiscount(name="20% off", percent=20)
    product.set_promotion(promotion)
    total_price = product.buy(quantity=2)
    assert total_price == 1600  # 1000 * 0.8 * 2


def test_third_one_free():
    """
    Test third one free promotion.
    """
    product = Product(name="USB Cable", price=10, quantity=10)
    promotion = ThirdOneFree(name="Buy 2 get 1 free")
    product.set_promotion(promotion)
    total_price = product.buy(quantity=4)
    assert total_price == 30  # 10 + 10 + 0 + 10


def test_remove_promotion():
    """
    Test removing a promotion from a product.
    """
    product = Product(name="Monitor", price=300, quantity=5)
    promotion = PercentDiscount(name="10% off", percent=10)
    product.set_promotion(promotion)
    product.set_promotion(None)  # Remove promotion
    total_price = product.buy(quantity=2)
    assert total_price == 600  # No discount applied


def test_limited_product_buy():
    """
    Test buying a limited product that exceeds the maximum limit.
    """
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(quantity=2)  # Exceeds the maximum limit
