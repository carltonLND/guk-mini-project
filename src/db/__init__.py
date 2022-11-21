from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from .couriers import map_couriers
from .orders import map_orders
from .products import map_products

DATA_PATH = "data/cafe.db"

mapper_registry = registry()


def setup_lite_db():
    engine = create_engine(f"sqlite:///{DATA_PATH}")
    mapper_registry.metadata.create_all(bind=engine, checkfirst=True)
    return engine


def create_lite_session():
    map_products(mapper_registry)
    map_couriers(mapper_registry)
    map_orders(mapper_registry)
    db = setup_lite_db()
    return sessionmaker(db)
