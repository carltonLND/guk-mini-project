from sqlalchemy import Column, ForeignKey, Integer, String, Table

from src.domain import Order

from .registry import mapper_registry

orders_table = Table(
    "orders",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_name", String, nullable=False),
    Column("customer_address", String, nullable=False),
    Column("customer_phone", Integer, nullable=False),
    Column("courier_id", Integer, ForeignKey("couriers.id"), nullable=False),
    Column("item_ids", String, nullable=False),
    Column("status", String, default="Preparing"),
)

mapper_registry.map_imperatively(Order, orders_table)
