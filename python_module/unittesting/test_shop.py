"""Module for testing Shop class of main.py file"""

import pytest
from main import Shop, Product


@pytest.fixture
def products():
    """Create list of 3 products for Shop"""
    return [
        Product('HDD', 30, 2),
        Product('GPU', 500, 1),
        Product('Memory', 15, 5)
]


@pytest.fixture
def product():
    """Create one product"""
    return Product('SSD', 100, 2)

@pytest.fixture
def shop_with_products(products):
    """Create shop filled with products from fixture"""
    return Shop(products)

def test_init(products):
    """Check if constructor works as expected"""
    new_shop1 = Shop(products)
    new_shop2 = Shop()
    new_shop3 = Shop(Product('TV', 1))
    assert new_shop1.products == products
    assert new_shop2.products == []
    assert len(new_shop3.products) == 1


def test_get_product_index(shop_with_products):
    """Check product's indexes"""
    assert shop_with_products._get_product_index('HDD') == 0
    assert shop_with_products._get_product_index('Memory') == 2

def test_add_product(shop_with_products):
    """Check if adding products works as expected"""
    prod = Product('Battery', 25, 2)
    shop_with_products.add_product(prod)
    assert prod in shop_with_products.products

def test_sell_product(shop_with_products):
    """Check if selling products works as expected"""
    with pytest.raises(ValueError):
        assert shop_with_products.sell_product('Memory', 2) == 30
        assert shop_with_products.sell_product('HDD') == 30
        # Delete the last HDD
        shop_with_products.sell_product('HDD')
        # Delete non existent product
        assert shop_with_products.sell_product('HDD') is None
        with pytest.raises(ValueError):
            # Sell more than in stock
            shop_with_products.sell_product('GPU', 100)
        