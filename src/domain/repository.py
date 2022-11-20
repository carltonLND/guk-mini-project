from abc import ABC, abstractmethod

from sqlalchemy import Table
from sqlalchemy.orm import Session


class ABCRepo(ABC):
    @abstractmethod
    def add(self, new_data):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def list(self) -> list:
        pass

    @abstractmethod
    def update(self, id, new_data):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class SQLProductRepo(ABCRepo):
    """Repository for handling session operations"""

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, model) -> None:
        """Adds model to database session"""
        self.session.add(model)

    def update(self, table, id, model):
        """Updates row with new changes"""
        self.session.query(table).filter_by(id=id).update(model)

    def delete(self, table: Table, id: int):
        """Deletes row in table by unique ID"""
        self.session.query(table).filter_by(id=id).delete()

    def get(self, table: Table, id: int):
        """Returns row in table based on filter reference"""
        return self.session.query(table).filter_by(id=id).one()

    def list(self, table: Table) -> list:
        """Returns list of all rows in table, or empty list"""
        return self.session.query(table).all()

    def save(self) -> None:
        """Commit transaction changes to database"""
        self.session.commit()

    def discard(self) -> None:
        """Discard changed in session transaction"""
        self.session.rollback()
