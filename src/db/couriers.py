from sqlalchemy import Column, Integer, String, Table

from src.domain import Courier

from .registry import mapper_registry

couriers_table = Table(
    "couriers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False),
)

mapper_registry.map_imperatively(Courier, couriers_table)
