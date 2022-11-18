from sqlalchemy import Column, Float, Integer, String, Table

from src.domain import Product

from .registry import mapper_registry

products_table = Table(
    "products",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("price", Float, nullable=False),
)

mapper_registry.map_imperatively(Product, products_table)
