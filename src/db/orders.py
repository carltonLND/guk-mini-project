from typing import Protocol

from .data import Data, DataList


class Order(Data):
    """Object representing an order"""

    def __init__(
        self,
        name: str,
        address: str,
        phone: int,
        courier: int,
        items: list[int],
        status: str = "Preparing",
    ) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.courier = courier
        self.status = status
        self.items = items

    def update(self, **kwargs):
        """Method for updating already existing attributes of self"""
        for key in kwargs.keys():
            if not hasattr(self, key):
                continue

            if not kwargs[key]:
                continue

            if key == "status":
                continue

            setattr(self, key, kwargs[key])

    def update_status(self, status: str):
        """Method for updating already existing attributes of self"""
        self.status = status

    def print_status_list(self, status_list: tuple[str]) -> None:
        for num, data in enumerate(status_list, 1):
            print(f"{num}) {data}")
        else:
            print()

    def __str__(self) -> str:
        string = ""
        for attribute, value in self.__dict__.items():
            if attribute == "status_list":
                continue

            string += f"{attribute}: {value} | "

        return string + "\n"


class CsvOrderHandlerProto(Protocol):
    def save_file(
        self, filename: str, fieldnames: list[str], data: list[Order]
    ) -> None:
        ...

    def load_file(self, filename: str) -> list[dict]:
        ...


class OrderList(DataList):
    """Object representing a collecting of Order types"""

    def __init__(self, *data_objects: Data) -> None:
        super().__init__(*data_objects)
        self.status_list = ("Preparing", "On the way", "Delivered")

    def create(self, **kwargs):
        self._data_list.append(Order(**kwargs))

    def save_csv(self, handler: CsvOrderHandlerProto):
        fieldnames = ["name", "address", "phone", "courier", "status", "items"]
        handler.save_file("orders", fieldnames, data=self._data_list)

    def load_csv(self, handler: CsvOrderHandlerProto):
        raw_data = handler.load_file("orders")
        if not raw_data:
            return

        for data in raw_data:
            self._data_list.append(Order(**data))
