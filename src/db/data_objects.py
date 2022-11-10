# TODO: Move derived data object and data list classes to app.py?
from abc import ABC, abstractmethod

from file_handlers.handler import Handler


class DataObject(ABC):
    # TODO: Don't even know if this going to work how i think
    # it is, will have to find out the hard way...
    def update(self, **kwargs):
        for key in kwargs.keys():
            if not hasattr(self, key):
                continue

            setattr(self, key, kwargs[key])

    def __repr__(self) -> str:
        data_repr = ""
        for attribute, value in self.__dict__.items():
            data_repr += f"{attribute}: {value}"

        return data_repr + "\n"


class Order(DataObject):
    def __init__(
        self,
        *,
        name: str,
        address: str,
        phone: int,
        courier: int,
    ) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.courier = courier
        self.status = "Preparing"


class Product(DataObject):
    def __init__(self, *, name: str) -> None:
        self.name = name


class Courier(DataObject):
    def __init__(self, *, name: str) -> None:
        self.name = name


class DataList(ABC):
    def __init__(self, *, file_handler: Handler) -> None:
        self._list = []
        self.handler = file_handler
        self.load_data()

    def add_data(self, *, data: DataObject) -> None:
        self._list.append(data)

    @abstractmethod
    def get_data(self, *, target: int) -> DataObject:
        pass

    @abstractmethod
    def delete_data(self, *, target: int):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @staticmethod
    def serialize(data: Product) -> str:
        product_string = ""
        for value in data.__dict__.values():
            product_string += value

        product_string += "\n"
        return product_string

    def __len__(self) -> int:
        return len(self._list)


class OrderList(DataList):
    def get_data(self, *, target: int) -> Order:
        return self._list[target]

    def delete_data(self, *, target: int) -> None:
        self._list.pop(target)

    def load_data(self):
        pass

    def save_data(self):
        pass

    def __repr__(self) -> str:
        if not self._list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self._list, 1):
            data_str += f"""{num}) Name: {data.name}
   Address: {data.address}
   Phone: {data.phone}
   Courier: {data.courier}
   Status: {data.status}\n"""
        return data_str.title()


class ProductList(DataList):
    def get_data(self, *, target: int) -> Product:
        return self._list[target]

    def delete_data(self, *, target: int) -> None:
        self._list.pop(target)

    def load_data(self) -> None:
        self._list += [
            Product(name=line) for line in self.handler.load_data("products")
        ]

    def save_data(self) -> None:
        lines = []
        for product in self._list:
            lines.append(self.serialize(product))

        self.handler.save_data("products", lines)

    def __repr__(self) -> str:
        if not self._list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self._list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()


class CourierList(DataList):
    def get_data(self, *, target: int) -> Courier:
        return self._list[target]

    def data_exists(self) -> bool:
        if not self._list:
            return False

        return True

    def delete_data(self, *, target: int) -> None:
        self._list.pop(target)

    def load_data(self) -> None:
        self._list += [
            Courier(name=line) for line in self.handler.load_data("couriers")
        ]

    def save_data(self) -> None:
        lines = []
        for courier in self._list:
            lines.append(self.serialize(courier))

        self.handler.save_data("couriers", lines)

    def __repr__(self) -> str:
        if not self._list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self._list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()
