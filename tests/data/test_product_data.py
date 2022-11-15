from src.db.products import Product, ProductList


def test_update_attributes():
    product = Product("Tea", 0.90)

    product.update(name="Coffee", price=1.25, fake="fake attr")

    assert product.name == "Coffee"
    assert product.price == 1.25
    assert not hasattr(product, "fake")


def test_product_list_length():
    product_list = ProductList()
    assert not product_list._data_list
    assert product_list.empty()

    product_list.create(name="Coffee", price=1.25)
    assert len(product_list._data_list) == 1


def test_product_list_get():
    product_list = ProductList()
    product_list.create(name="Coffee", price=1.25)

    product = product_list.get(0)
    assert type(product) is Product
    assert product.name == "Coffee"
    assert product.price == 1.25


def test_product_list_delete():
    product_list = ProductList()
    product_list.create(name="Coffee", price=1.25)

    product = product_list.get(0)

    assert product in product_list._data_list
    product_list.delete(0)
    assert product not in product_list._data_list
