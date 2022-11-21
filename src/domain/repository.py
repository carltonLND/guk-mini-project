import copy
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from src.file_handlers import CsvHandler

from .courier import Courier
from .order import Order
from .product import Product


class ABCRepo(ABC):
    @abstractmethod
    def add(self, row):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def all(self) -> list:
        pass

    @abstractmethod
    def update(self, id, row):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class SQLRepo(ABCRepo):
    """Repository for handling session operations"""

    def __init__(self, table, session: Session) -> None:
        self.table = table
        self.session = session

    def add(self, row) -> None:
        """Adds row to database session"""
        self.session.add(row)

    def update(self, id, row):
        """Updates row with new changes"""
        self.session.query(self.table).filter_by(id=id).update(row)

    def delete(self, id: int):
        """Deletes row in table by unique ID"""
        self.session.query(self.table).filter_by(id=id).delete()

    def get(self, id: int):
        """Returns row in table based on filter reference"""
        return self.session.query(self.table).filter_by(id=id).one()

    def all(self) -> list:
        """Returns list of all rows in table, or empty list"""
        return self.session.query(self.table).all()

    def save(self) -> None:
        """Commit transaction changes to database"""
        self.session.commit()

    def discard(self) -> None:
        """Discard changed in session transaction"""
        self.session.rollback()


class CsvRepo(ABCRepo):
    def __init__(
        self,
        domain: type[Product] | type[Courier] | type[Order],
        filename: str,
        fieldnames: list[str],
    ) -> None:
        self.Domain = domain
        self.handler = CsvHandler(filename, fieldnames)
        self._data = self._serialize(self.handler.load_file())
        self._backup_data = copy.deepcopy(self._data)

    def add(self, row):
        self._data.append(row)

    def update(self, id, row) -> None:
        self._data[id] = row

    def delete(self, id) -> None:
        self._data.pop(id)

    def get(self, id):
        return self._data[id]

    def all(self) -> list:
        return self._data

    def save(self) -> None:
        self.handler.save_file(self._data)
        self._backup_data = copy.deepcopy(self._data)

    def discard(self) -> None:
        self._data = copy.deepcopy(self._backup_data)

    def _serialize(self, data: list[dict]):
        serialized_data = []
        for obj in data:
            serialized_data.append(self.Domain(**obj))
        return serialized_data
