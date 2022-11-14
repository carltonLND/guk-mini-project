from abc import ABC, abstractmethod

from file_handlers import CsvHandler


class ABCData(ABC):
    """Abstract interface representing data"""

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ABCDataList(ABC):
    """Abstract interface represnting a collection of DataABC objects"""

    @abstractmethod
    def __init__(self, *data_objects: ABCData) -> None:
        pass

    @abstractmethod
    def get(self, index: int) -> list:
        pass

    @abstractmethod
    def delete(self, index: int) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Data(ABCData):
    """Class to build out recurring functionality of ABCData objects"""

    def __init__(self, *_) -> None:
        pass

    def update(self, **kwargs):
        """Method for updating already existing attributes of self"""
        for key in kwargs.keys():
            if not hasattr(self, key):
                continue

            if not kwargs[key]:
                continue

            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        string = ""
        for attribute, value in self.__dict__.items():
            string += f"{attribute}: {value} | "

        return string + "\n"


class DataList(ABCDataList):
    """Class to represent and manipulate collections of ABCData types"""

    _data_list: list

    def __init__(self, *data_objects: Data) -> None:
        self._data_list = [*data_objects]

    def get(self, index: int) -> list:
        return self._data_list[index]

    def delete(self, index: int) -> None:
        self._data_list.pop(index)

    def empty(self):
        return True if not self._data_list else False

    def __len__(self) -> int:
        return len(self._data_list) + 1

    def __str__(self) -> str:
        if not self._data_list:
            return "No Data!\n"

        string = ""
        for num, data in enumerate(self._data_list, 1):
            string += f"{num}) {data}"

        return string


class ABCDataController(ABC):
    """Abstract class for DataController's"""


class DataController(ABCDataController):
    """Controller for accessing DataList objects"""

    def __init__(self, handler: CsvHandler, **data_lists: ABCDataList) -> None:
        for name, data_list in data_lists.items():
            setattr(self, name, data_list)
        self.handler = handler

    def load_csv(self):
        print("Loading...\n")
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.load_csv(self.handler)

    def save_csv(self):
        print("Saving...\n")
        for name, data_list in self.__dict__.items():
            if name == "handler":
                continue

            data_list.save_csv(self.handler)
