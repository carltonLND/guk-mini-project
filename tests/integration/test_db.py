import pytest
from sqlalchemy.orm import clear_mappers

import src.db as db
from src.domain.product import Product
from src.domain.repository import SQLiteRepo

db.DB_DATA_PATH = ":memory:"


@pytest.fixture
def sql_repo():
    clear_mappers()
    db.mapper_registry.metadata.clear()
    Session = db.create_lite_session()
    return SQLiteRepo(Product, Session())


def test_empty_table(sql_repo):
    assert sql_repo.all() == []


def test_row_added(sql_repo):
    assert sql_repo.all() == []
    sql_repo.add(Product(name="Coffee", price=1.90))
    assert sql_repo.all() != []


def test_discard_changes(sql_repo):
    sql_repo.add(Product(name="Coffee", price=1.90))
    assert sql_repo.all() != []
    sql_repo.discard()
    assert sql_repo.all() == []


def test_get_row_not_found(sql_repo):
    assert sql_repo.get(120938) == None


def test_row_found(sql_repo):
    sql_repo.add(Product(name="Coffee", price=1.90))
    row = sql_repo.get(1)
    assert row != None
    assert row.id == 1
    assert row.name == "Coffee"
    assert row.price == 1.90


def test_row_update(sql_repo):
    sql_repo.add(Product(name="Coffee", price=1.90))
    changes = {"name": "Cake"}
    assert sql_repo.get(1).name == "Coffee"
    sql_repo.update(1, changes)
    assert sql_repo.get(1).name == "Cake"


def test_row_delete(sql_repo):
    sql_repo.add(Product(name="Coffee", price=1.90))
    assert sql_repo.get(1) != None
    sql_repo.delete(1)
    assert sql_repo.get(1) == None
