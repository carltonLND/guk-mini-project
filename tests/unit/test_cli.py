from unittest.mock import Mock, patch

import pytest
from typer import Abort

import src.cli_menu.product as p

test = Mock()
test.all.return_value = ["hello"]


@pytest.fixture
def mock_product_1():
    product = Mock()
    product.id = 1
    product.name = "tea"
    product.price = 1.1
    return product


@pytest.fixture
def mock_product_2():
    product = Mock()
    product.id = 2
    product.name = "coffee"
    product.price = 1.60
    return product


@pytest.fixture
def mock_repo():
    product_1 = Mock()
    product_1.id = 1
    product_1.name = "tea"
    product_1.price = 1.1

    product_2 = Mock()
    product_2.id = 2
    product_2.name = "coffee"
    product_2.price = 1.60

    mock_repo = Mock()
    mock_repo.all.return_value = [product_1, product_2]
    return mock_repo


@pytest.fixture
def mock_empty_repo():
    mock_repo = Mock()
    mock_repo.all.return_value = []
    return mock_repo


@patch("builtins.print")
@patch("src.cli_menu.product.repo_setup")
def test_no_rows(mock_setup, mock_print, mock_empty_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_empty_repo

    with pytest.raises(Abort) as e:
        p.product_default(ctx)

    assert mock_print.call_args.args == ("No Products!",)


@patch("builtins.print")
@patch("src.cli_menu.product.repo_setup")
def test_print_products(mock_setup, mock_print, mock_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_repo

    p.product_default(ctx)

    assert mock_print.call_count == 2


@patch("src.cli_menu.product.repo_setup")
def test_return_early_if_subcommand(mock_setup):
    ctx = Mock()
    ctx.invoked_subcommand = "add"

    assert p.product_default(ctx) == None
