from typing import Protocol


class CsvAnyHandlerProto(Protocol):
    def save_file(self, filename: str, fieldnames: list[str], data: list) -> None:
        ...

    def load_file(self, filename: str) -> list[dict]:
        ...


class DataListProto(Protocol):
    def save_csv(self, handler: CsvAnyHandlerProto) -> None:
        ...

    def load_csv(self, handler: CsvAnyHandlerProto) -> None:
        ...


class CsvDataController:
    """Controller for accessing DataList objects"""

    def __init__(
        self, handler: CsvAnyHandlerProto, **data_lists: DataListProto
    ) -> None:
        for name, data_list in data_lists.items():
            setattr(self, name, data_list)
        self.handler = handler

    def load(self):
        print("Loading...\n")
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.load_csv(self.handler)

    def save(self):
        print("Saving...\n")
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.save_csv(self.handler)
