from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from .couriers import map_couriers
from .orders import map_orders
from .products import map_products

mapper_registry = registry()

map_products(mapper_registry)
map_couriers(mapper_registry)
map_orders(mapper_registry)


def setup_lite_db():
    engine = create_engine(f"sqlite:///data/cafe.db")
    mapper_registry.metadata.create_all(bind=engine, checkfirst=True)
    return engine


def create_lite_session():
    db = setup_lite_db()
    return sessionmaker(db)
