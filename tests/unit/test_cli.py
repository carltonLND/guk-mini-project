from unittest.mock import Mock, patch

import pytest
import typer

import src.cli_menu.product as p


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

    with pytest.raises(typer.Abort):
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


@patch("builtins.print")
def test_return_early_if_subcommand(mock_print):
    ctx = Mock()
    ctx.invoked_subcommand = "add"

    assert p.product_default(ctx) == None
    assert mock_print.call_count == 0


@patch("src.cli_menu.product.confirm")
@patch("src.cli_menu.product.ensure_float")
@patch("src.cli_menu.product.typer.prompt")
@patch("src.cli_menu.product.repo_setup")
def test_confirm_add_product(
    mock_setup, mock_prompt, mock_ensure_float, mock_confirm, mock_empty_repo
):
    mock_setup.return_value = mock_empty_repo
    mock_prompt.return_value = "Cake"
    mock_ensure_float.return_value = 3.10
    mock_confirm.return_value = True

    assert p.product_add() == None


@patch("src.cli_menu.product.confirm")
@patch("src.cli_menu.product.ensure_float")
@patch("src.cli_menu.product.typer.prompt")
@patch("src.cli_menu.product.repo_setup")
def test_no_confirm_add_product(
    mock_setup, mock_prompt, mock_ensure_float, mock_confirm, mock_empty_repo
):
    mock_setup.return_value = mock_empty_repo
    mock_prompt.return_value = "Cake"
    mock_ensure_float.return_value = 3.10
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        p.product_add()


@patch("src.cli_menu.product.confirm")
@patch("src.cli_menu.product.ensure_int")
@patch("src.cli_menu.product.ensure_float")
@patch("src.cli_menu.product.typer.prompt")
@patch("src.cli_menu.product.repo_setup")
def test_update_product(
    mock_setup,
    mock_prompt,
    mock_ensure_float,
    mock_ensure_int,
    mock_confirm,
    mock_repo,
):
    mock_setup.return_value = mock_repo
    mock_prompt.return_value = "Sandwhich"
    mock_ensure_float.return_value = 1.49
    mock_ensure_int.return_value = 2
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        p.product_update()

    assert mock_repo.update.call_args.args == (2, {"name": "Sandwhich", "price": 1.49})
    assert mock_repo.discard.call_count == 1
    assert mock_repo.save.call_count == 0


@patch("src.cli_menu.product.confirm")
@patch("src.cli_menu.product.ensure_int")
@patch("src.cli_menu.product.repo_setup")
def test_delete_product(
    mock_setup,
    mock_ensure_int,
    mock_confirm,
    mock_repo,
):
    mock_setup.return_value = mock_repo
    mock_ensure_int.return_value = 1
    mock_confirm = True

    p.product_delete()

    assert mock_repo.delete.call_args.args == (1,)
    assert mock_repo.save.call_count == 1
    assert mock_repo.discard.call_count == 0
