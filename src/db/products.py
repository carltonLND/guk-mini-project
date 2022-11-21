from sqlalchemy import Column, Float, Integer, String, Table

from src.domain import Product


def map_products(registry):
    """Imperatively maps Product object to DB table"""

    products_table = Table(
        "products",
        registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String, nullable=False),
        Column("price", Float, nullable=False),
    )

    registry.map_imperatively(Product, products_table)
