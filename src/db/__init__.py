from sqlalchemy import create_engine

from .couriers import couriers_table
from .orders import orders_table
from .products import products_table
from .registry import mapper_registry


def setup_lite_db(db_path: str):
    engine = create_engine(f"sqlite:///{db_path}")
    mapper_registry.metadata.create_all(bind=engine, checkfirst=True)
    return engine
