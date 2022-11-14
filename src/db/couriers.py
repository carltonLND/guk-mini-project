from file_handlers import CsvHandler

from .data import Data, DataList


class Courier(Data):
    """Object representing a courier"""

    def __init__(self, name: str, phone: int) -> None:
        self.name = name
        self.phone = phone


class CourierList(DataList):
    """Object representing a collection of Courier types"""

    def create(self, **kwargs):
        self._data_list.append(Courier(**kwargs))

    def save_csv(self, handler: CsvHandler):
        fieldnames = ["name", "phone"]
        handler.save_file("couriers", fieldnames, data=self._data_list)

    def load_csv(self, handler: CsvHandler):
        raw_data = handler.load_file("couriers")
        if not raw_data:
            return

        for data in raw_data:
            self._data_list.append(Courier(**data))
