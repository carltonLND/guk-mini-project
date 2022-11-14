from abc import ABC, abstractmethod


class ABCHandler(ABC):
    """Abstract interface for derived file handler objects"""

    @abstractmethod
    def load_file(self, filename: str) -> list[dict]:
        """Reads data from file and returns a list"""
        pass

    @abstractmethod
    def save_file(self, filename: str, data: list) -> None:
        """Writes data from list into file"""
        pass

    @abstractmethod
    def _create_file(self, file) -> None:
        """Creates file if it doesn't already exist"""
        pass


class Handler(ABCHandler):
    """Handler base class for implementing common methods"""

    def _create_file(self, file) -> None:
        open(file, "x").close()
