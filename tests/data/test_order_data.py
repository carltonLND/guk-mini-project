import pytest

from src.db.orders import Order, OrderList


@pytest.fixture
def default_order():
    return Order(
        name="Carlton", address="Somewhere", phone=12345, courier=0, items=[1, 1, 1]
    )


@pytest.fixture
def order_list_empty():
    return OrderList()


@pytest.fixture
def order_list_not_empty():
    return OrderList(
        Order(
            name="Carlton", address="Somewhere", phone=12345, courier=0, items=[1, 1, 1]
        )
    )


def test_order_status_default(default_order):
    assert default_order.status == "Preparing"


def test_update_attributes(default_order):
    default_order.update(name="Bob Ross", fake="hello")
    assert default_order.name == "Bob Ross"
    assert default_order.phone == 12345
    assert not hasattr(default_order, "fake")


def test_order_list_length(order_list_not_empty):
    assert not order_list_not_empty.empty()
    assert len(order_list_not_empty._data_list) == 1


def test_order_list_get(order_list_not_empty):
    order = order_list_not_empty.get(0)
    assert type(order) is Order
    assert order.name == "Carlton"
    assert order.phone == 12345


def test_order_list_delete(order_list_not_empty):
    order_list_not_empty.delete(0)
    assert order_list_not_empty.empty()


def test_order_update_status(order_list_not_empty, default_order):
    default_order.update_status(order_list_not_empty.status_list[2])
    assert default_order.status == "Delivered"
