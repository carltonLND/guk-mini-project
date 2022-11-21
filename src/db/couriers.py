from sqlalchemy import Column, Integer, String, Table

from src.domain import Courier


def map_couriers(registry):
    """Imperatively maps Courier object to DB table"""

    couriers_table = Table(
        "couriers",
        registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
        Column("phone", Integer, nullable=False),
    )

    registry.map_imperatively(Courier, couriers_table)
