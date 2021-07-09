"""Module for testing Product class of main.py file"""


import pytest
from main import Product


@pytest.fixture
def product():
    """Create product SSD for 100 USD with 2 items in stock"""
    return Product('SSD', 100, 2)


def test_product_init():
    """Check if default value holds true"""
    assert Product(title='Screen', price=500).quantity == 1


def test_product_subtract_quantity(product):
    """"Check if subtracting elements works in expected way"""
    product.subtract_quantity()
    assert product.quantity == 1
    product.subtract_quantity(0)
    assert product.quantity == 1
    with pytest.raises(ValueError):
        # Subtract more than products in stock
        product.subtract_quantity(-100)


def test_product_add_quantity(product):
    """Check if adding elements works in expected way"""
    product.add_quantity(1)
    assert product.quantity == 3
    with pytest.raises(ValueError):
        # Add negative value of products
        product.add_quantity(-1)


def test_product_change_price(product):
    """Check if setting different price tags works in expected way"""
    product.change_price(500)
    assert product.price == 500
    with pytest.raises(ValueError):
        # Set negative price
        product.change_price(-500)
