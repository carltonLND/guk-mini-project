from unittest.mock import Mock, patch

import pytest

from src.db.products import Product, ProductList


def test_update_attributes():
    product = Product("Tea", 0.90)

    product.update(name="Coffee", price=1.25, fake="fake attr")

    assert product.name == "Coffee"
    assert product.price == 1.25
    assert not hasattr(product, "fake")


def test_product_list_():
    product_list = ProductList()
    assert not product_list._data_list
    assert product_list.empty()

    product_list.create(name="Coffee", price=1.25)
    assert len(product_list._data_list) == 1
