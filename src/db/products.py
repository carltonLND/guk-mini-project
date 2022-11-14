from file_handlers import CsvHandler

from .data import Data, DataList


class Product(Data):
    """Object representing a product"""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class ProductList(DataList):
    """Object representing a collection of Product types"""

    def create(self, **kwargs):
        self._data_list.append(Product(**kwargs))

    def save_csv(self, handler: CsvHandler):
        fieldnames = ["name", "price"]
        handler.save_file("products", fieldnames, data=self._data_list)

    def load_csv(self, handler: CsvHandler):
        raw_data = handler.load_file("products")
        if not raw_data:
            return

        for data in raw_data:
            self._data_list.append(Product(**data))
