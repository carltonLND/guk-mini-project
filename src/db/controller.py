from typing import Protocol

from .data import ABCData, ABCDataController


class CsvHandlerProto(Protocol):
    def save_file(self, filename: str, fieldnames: list[str], data: list) -> None:
        ...

    def load_file(self, filename: str) -> list[dict]:
        ...


class CsvDataListProto(Protocol):
    def create(self, **kwargs) -> None:
        ...

    def get(self, index: int) -> ABCData:
        ...

    def delete(self, index: int) -> None:
        ...

    def empty(self) -> bool:
        ...

    def save_csv(self, handler: CsvHandlerProto) -> None:
        ...

    def load_csv(self, handler: CsvHandlerProto) -> None:
        ...


class CsvDataController(ABCDataController):
    """Controller for accessing DataList objects"""

    def __init__(
        self, handler: CsvHandlerProto, **data_lists: CsvDataListProto
    ) -> None:
        for name, data_list in data_lists.items():
            if name == "products":
                self.products = data_list
            if name == "orders":
                self.orders = data_list
            if name == "couriers":
                self.couriers = data_list

            else:
                setattr(self, name, data_list)

        self.handler = handler

    def load(self):
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.load_csv(self.handler)

    def save(self):
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.save_csv(self.handler)
