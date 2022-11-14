from typing import Protocol

from .data import Data, DataList


class Product(Data):
    """Object representing a product"""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class CsvProductHandlerProto(Protocol):
    def save_file(
        self, filename: str, fieldnames: list[str], data: list[Product]
    ) -> None:
        ...

    def load_file(self, filename: str) -> list[dict]:
        ...


class ProductList(DataList):
    """Object representing a collection of Product types"""

    def create(self, **kwargs):
        self._data_list.append(Product(**kwargs))

    def save_csv(self, handler: CsvProductHandlerProto):
        fieldnames = ["name", "price"]
        handler.save_file("products", fieldnames, data=self._data_list)

    def load_csv(self, handler: CsvProductHandlerProto):
        raw_data = handler.load_file("products")
        if not raw_data:
            return

        for data in raw_data:
            self._data_list.append(Product(**data))
