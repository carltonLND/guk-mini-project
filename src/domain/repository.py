from sqlalchemy import Table
from sqlalchemy.orm import Session


class Repository:
    """Repository for handling session operations"""

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, model) -> None:
        """Adds model to database session"""
        self.session.add(model)

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
