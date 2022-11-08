from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    @abstractmethod
    def load_data(self, file_name: str) -> list:
        pass

    @abstractmethod
    def save_data(self, file_name: str, data: list) -> None:
        pass
