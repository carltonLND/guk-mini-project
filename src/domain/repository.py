from abc import ABC, abstractmethod

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

    def list(self) -> list:
        """Returns list of all rows in table, or empty list"""
        return self.session.query(self.table).all()

    def save(self) -> None:
        """Commit transaction changes to database"""
        self.session.commit()

    def discard(self) -> None:
        """Discard changed in session transaction"""
        self.session.rollback()
