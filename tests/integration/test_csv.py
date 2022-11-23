import pytest

import src.file_handlers.csv_handler as csv_db
from src.domain.product import Product
from src.domain.repository import CsvRepo

csv_db.CSV_DATA_PATH = "tests/integration/test_data/"


@pytest.fixture
def csv_repo():
    return CsvRepo(Product, "test_products", ["id", "name", "price"])


def test_empty_file(csv_repo):
    assert csv_repo.all() == []


def test_row_added(csv_repo):
    assert csv_repo.all() == []
    csv_repo.add(Product(name="Coffee", price=1.90))
    assert csv_repo.all() != []


def test_discard_changes(csv_repo):
    csv_repo.add(Product(name="Coffee", price=1.90))
    assert csv_repo.all() != []
    csv_repo.discard()
    assert csv_repo.all() == []


def test_get_row_not_found(csv_repo):
    assert csv_repo.get(120938) == None


def test_row_found(csv_repo):
    csv_repo.add(Product(id=1, name="Coffee", price=1.90))
    row = csv_repo.get(1)
    assert row != None
    assert row.id == 1
    assert row.name == "Coffee"
    assert row.price == 1.90


def test_row_update(csv_repo):
    csv_repo.add(Product(id=1, name="Coffee", price=1.90))
    changes = {"name": "Cake"}
    assert csv_repo.get(1).name == "Coffee"
    csv_repo.update(1, changes)
    assert csv_repo.get(1).name == "Cake"


def test_data_saved(csv_repo):
    csv_repo.add(Product(name="Coffee", price=1.90))
    csv_repo.save()


def test_row_delete(csv_repo):
    assert csv_repo.get(1) != None
    csv_repo.delete(1)
    assert csv_repo.get(1) == None
    csv_repo.save()
