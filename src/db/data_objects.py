from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from file_handlers.handler import Handler


class DataObject(ABC):
    # TODO: Don't even know if this going to work how i think
    # it is, will have to find out the hard way...
    def update(self, **kwargs):
        for key in kwargs.keys():
            if not getattr(self, key):
                continue

            setattr(self, key, kwargs[key])


@dataclass(kw_only=True, slots=True)
class Order(DataObject):
    name: str
    address: str
    phone: int
    courier: int
    status: str = field(init=False, default="Preparing")


@dataclass(kw_only=True, slots=True)
class Product(DataObject):
    name: str


@dataclass(kw_only=True, slots=True)
class Courier(DataObject):
    name: str


class DataList(ABC):
    def __init__(self, *, file_handler: Handler) -> None:
        self._list = []
        self.handler = file_handler
        self.load_data()

    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

    def __len__(self) -> int:
        return len(self._list)


class OrderList(DataList):
    def add_data(self, *, order: Order) -> None:
        self._list.append(order)

    def get_data(self, *, target: int) -> Order:
        return self._list[target]

    def delete_data(self, *, target: int) -> None:
        self._list.pop(target)

    def load_data(self):
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
    def add_data(self, *, product: Product) -> None:
        self._list.append(product)

    def get_data(self, *, target: int) -> Product:
        return self._list[target]

    def delete_data(self, *, target: int) -> None:
        self._list.pop(target)

    def load_data(self) -> None:
        self._list += [
            Product(name=line) for line in self.handler.load_data("products")
        ]

    def __repr__(self) -> str:
        if not self._list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self._list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()


class CourierList(DataList):
    def add_data(self, *, courier: Courier) -> None:
        self._list.append(courier)

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

    def __repr__(self) -> str:
        if not self._list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self._list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()
