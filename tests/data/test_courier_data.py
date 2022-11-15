from src.db.couriers import Courier, CourierList


def test_update_attributes():
    courier = Courier("Tea", 12512)

    courier.update(name="Patrick", phone=125, fake="fake attr")

    assert courier.name == "Patrick"
    assert courier.phone == 125
    assert not hasattr(courier, "fake")


def test_courier_list_length():
    courier_list = CourierList()
    assert not courier_list._data_list
    assert courier_list.empty()

    courier_list.create(name="Patrick", phone=125)
    assert len(courier_list._data_list) == 1


def test_courier_list_get():
    courier_list = CourierList()
    courier_list.create(name="Patrick", phone=125)

    courier = courier_list.get(0)
    assert type(courier) is Courier
    assert courier.name == "Patrick"
    assert courier.phone == 125


def test_courier_list_delete():
    courier_list = CourierList()
    courier_list.create(name="Patrick", phone=125)

    courier = courier_list.get(0)

    assert courier in courier_list._data_list
    courier_list.delete(0)
    assert courier not in courier_list._data_list
