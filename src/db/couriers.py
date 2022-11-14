from typing import Protocol

from .data import Data, DataList


class Courier(Data):
    """Object representing a courier"""

    def __init__(self, name: str, phone: int) -> None:
        self.name = name
        self.phone = phone


class CsvCourierHandlerProto(Protocol):
    def save_file(
        self, filename: str, fieldnames: list[str], data: list[Courier]
    ) -> None:
        ...

    def load_file(self, filename: str) -> list[dict]:
        ...


class CourierList(DataList):
    """Object representing a collection of Courier types"""

    def create(self, **kwargs):
        self._data_list.append(Courier(**kwargs))

    def save_csv(self, handler: CsvCourierHandlerProto):
        fieldnames = ["name", "phone"]
        handler.save_file("couriers", fieldnames, data=self._data_list)

    def load_csv(self, handler: CsvCourierHandlerProto):
        raw_data = handler.load_file("couriers")
        if not raw_data:
            return

        for data in raw_data:
            self._data_list.append(Courier(**data))
