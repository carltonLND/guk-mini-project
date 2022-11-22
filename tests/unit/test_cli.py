from unittest.mock import Mock, patch

import pytest
import typer

import src.cli_menu.courier as c
import src.cli_menu.order as o
import src.cli_menu.product as p


@pytest.fixture
def mock_product_repo():
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
def mock_courier_repo():
    courier_1 = Mock()
    courier_1.id = 1
    courier_1.name = "Patrick"
    courier_1.phone = 192837412

    courier_2 = Mock()
    courier_2.id = 2
    courier_2.name = "Evil Patrick"
    courier_2.phone = 999999999

    mock_repo = Mock()
    mock_repo.all.return_value = [courier_1, courier_2]
    return mock_repo


@pytest.fixture
def mock_order_repo():
    order_1 = Mock()
    order_1.id = 1
    order_1.customer_name = "Patrick"
    order_1.customer_address = "Watching the world cup"
    order_1.customer_phone = 987654321
    order_1.courier_id = 1
    order_1.item_ids = "1, 2"
    order_1.status = "1 (Preparing)"

    order_2 = Mock()
    order_2.id = 2
    order_2.customer_name = "Evil Patrick"
    order_2.customer_address = "Crying over Argentina"
    order_2.customer_phone = 123456789
    order_2.courier_id = 1
    order_2.item_ids = "2, 2, 2, 2"
    order_2.status = "3 (Delivered)"

    mock_repo = Mock()
    mock_repo.all.return_value = [order_1, order_2]
    return mock_repo


@pytest.fixture
def mock_empty_repo():
    mock_repo = Mock()
    mock_repo.all.return_value = []
    return mock_repo


@patch("builtins.print")
@patch("src.cli_menu.product.repo_setup")
def test_no_product_rows(mock_setup, mock_print, mock_empty_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_empty_repo

    with pytest.raises(typer.Abort):
        p.product_default(ctx)

    assert mock_print.call_args.args == ("No Products!",)


@patch("builtins.print")
@patch("src.cli_menu.product.repo_setup")
def test_print_products(mock_setup, mock_print, mock_product_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_product_repo

    p.product_default(ctx)

    assert mock_print.call_count == 2


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
    assert mock_empty_repo.add.call_count == 1
    assert mock_confirm.call_count == 1
    assert mock_empty_repo.save.call_count == 1


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
    mock_product_repo,
):
    mock_setup.return_value = mock_product_repo
    mock_prompt.return_value = "Sandwhich"
    mock_ensure_float.return_value = 1.49
    mock_ensure_int.return_value = 2
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        p.product_update()

    assert mock_product_repo.update.call_args.args == (
        2,
        {"name": "Sandwhich", "price": 1.49},
    )
    assert mock_product_repo.discard.call_count == 1
    assert mock_product_repo.save.call_count == 0


@patch("src.cli_menu.product.confirm")
@patch("src.cli_menu.product.ensure_int")
@patch("src.cli_menu.product.repo_setup")
def test_delete_product(
    mock_setup,
    mock_ensure_int,
    mock_confirm,
    mock_product_repo,
):
    mock_setup.return_value = mock_product_repo
    mock_ensure_int.return_value = 1
    mock_confirm.return_value = True

    p.product_delete()

    assert mock_product_repo.delete.call_args.args == (1,)
    assert mock_product_repo.save.call_count == 1
    assert mock_product_repo.discard.call_count == 0


@patch("builtins.print")
@patch("src.cli_menu.courier.repo_setup")
def test_no_courier_rows(mock_setup, mock_print, mock_empty_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_empty_repo

    with pytest.raises(typer.Abort):
        c.courier_default(ctx)

    assert mock_print.call_args.args == ("No Couriers!",)


@patch("builtins.print")
@patch("src.cli_menu.courier.repo_setup")
def test_print_couriers(mock_setup, mock_print, mock_courier_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = mock_courier_repo

    c.courier_default(ctx)

    assert mock_print.call_count == 2


@patch("builtins.print")
def test_return_early_if_subcommand(mock_print):
    ctx = Mock()
    ctx.invoked_subcommand = "add"

    assert p.product_default(ctx) == None
    assert c.courier_default(ctx) == None
    assert o.order_default(ctx) == None
    assert mock_print.call_count == 0


@patch("src.cli_menu.courier.confirm")
@patch("src.cli_menu.courier.ensure_int")
@patch("src.cli_menu.courier.typer.prompt")
@patch("src.cli_menu.courier.repo_setup")
def test_confirm_add_courier(
    mock_setup, mock_prompt, mock_ensure_int, mock_confirm, mock_empty_repo
):
    mock_setup.return_value = mock_empty_repo
    mock_prompt.return_value = "Good Patrick"
    mock_ensure_int.return_value = 191919191
    mock_confirm.return_value = True

    assert c.courier_add() == None
    assert mock_empty_repo.add.call_count == 1
    assert mock_confirm.call_count == 1
    assert mock_empty_repo.save.call_count == 1


@patch("src.cli_menu.courier.confirm")
@patch("src.cli_menu.courier.ensure_int")
@patch("src.cli_menu.courier.typer.prompt")
@patch("src.cli_menu.courier.repo_setup")
def test_no_confirm_add_courier(
    mock_setup, mock_prompt, mock_ensure_int, mock_confirm, mock_empty_repo
):
    mock_setup.return_value = mock_empty_repo
    mock_prompt.return_value = "Good Patrick"
    mock_ensure_int.return_value = 191919191
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        c.courier_add()


@patch("src.cli_menu.courier.confirm")
@patch("src.cli_menu.courier.ensure_int")
@patch("src.cli_menu.courier.typer.prompt")
@patch("src.cli_menu.courier.repo_setup")
def test_update_courier(
    mock_setup,
    mock_prompt,
    mock_ensure_int,
    mock_confirm,
    mock_product_repo,
):
    mock_setup.return_value = mock_product_repo
    mock_prompt.return_value = "Good Patrick"
    mock_ensure_int.side_effect = [2, 76767676]
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        c.courier_update()

    assert mock_product_repo.update.call_args.args == (
        2,
        {"name": "Good Patrick", "phone": 76767676},
    )
    assert mock_product_repo.discard.call_count == 1
    assert mock_product_repo.save.call_count == 0


@patch("src.cli_menu.courier.confirm")
@patch("src.cli_menu.courier.ensure_int")
@patch("src.cli_menu.courier.repo_setup")
def test_delete_courier(
    mock_setup,
    mock_ensure_int,
    mock_confirm,
    mock_courier_repo,
):
    mock_setup.return_value = mock_courier_repo
    mock_ensure_int.return_value = 1
    mock_confirm.return_value = True

    c.courier_delete()

    assert mock_courier_repo.delete.call_args.args == (1,)
    assert mock_courier_repo.save.call_count == 1
    assert mock_courier_repo.discard.call_count == 0


@patch("builtins.print")
@patch("src.cli_menu.order.repo_setup")
def test_no_order_rows(mock_setup, mock_print, mock_empty_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = None, None, mock_empty_repo

    with pytest.raises(typer.Abort):
        o.order_default(ctx)

    assert mock_print.call_args.args == ("No Orders!",)


@patch("builtins.print")
@patch("src.cli_menu.order.repo_setup")
def test_print_orders(mock_setup, mock_print, mock_order_repo):
    ctx = Mock()
    ctx.invoked_subcommand = None
    mock_setup.return_value = None, None, mock_order_repo

    o.order_default(ctx)

    assert mock_print.call_count == 2


@patch("src.cli_menu.order.confirm")
@patch("src.cli_menu.order.select_items")
@patch("src.cli_menu.order.select_courier")
@patch("src.cli_menu.order.ensure_int")
@patch("src.cli_menu.order.typer.prompt")
@patch("src.cli_menu.order.repo_setup")
def test_confirm_add_order(
    mock_setup,
    mock_prompt,
    mock_ensure_int,
    mock_select_courier,
    mock_select_items,
    mock_confirm,
    mock_empty_repo,
    mock_product_repo,
    mock_courier_repo,
):
    mock_setup.return_value = mock_product_repo, mock_courier_repo, mock_empty_repo
    mock_prompt.side_effect = ["Good Patrick", "Patrick's Python Podcast"]
    mock_ensure_int.return_value = 111111111
    mock_select_courier.return_value = 2
    mock_select_items.return_value = "1, 1, 1"
    mock_confirm.return_value = True

    assert o.order_add() == None
    assert mock_empty_repo.add.call_count == 1
    assert mock_confirm.call_count == 1
    assert mock_empty_repo.save.call_count == 1


@patch("builtins.print")
@patch("src.cli_menu.order.repo_setup")
def test_no_couriers_add_order(
    mock_setup,
    mock_print,
    mock_empty_repo,
):
    mock_setup.return_value = None, mock_empty_repo, None

    with pytest.raises(typer.Abort):
        o.order_add()

    assert mock_print.call_count == 1
    assert mock_print.call_args.args == ("No Couriers!",)


@patch("builtins.print")
@patch("src.cli_menu.order.repo_setup")
def test_no_products_add_order(
    mock_setup,
    mock_print,
    mock_empty_repo,
    mock_courier_repo,
):
    mock_setup.return_value = mock_empty_repo, mock_courier_repo, None

    with pytest.raises(typer.Abort):
        o.order_add()

    assert mock_print.call_count == 1
    assert mock_print.call_args.args == ("No Products!",)


@patch("src.cli_menu.order.confirm")
@patch("src.cli_menu.order.select_status")
@patch("src.cli_menu.order.ensure_int")
@patch("src.cli_menu.order.repo_setup")
def test_update_order_status(
    mock_setup, mock_ensure_int, mock_select_status, mock_confirm, mock_order_repo
):
    mock_setup.return_value = None, None, mock_order_repo
    mock_ensure_int.return_value = 1
    mock_select_status.return_value = "2 (On the way)"
    mock_confirm.return_value = True

    o.order_status()

    assert mock_order_repo.update.call_count == 1
    assert mock_order_repo.update.call_args.args == (1, {"status": "2 (On the way)"})


@patch("src.cli_menu.order.confirm")
@patch("src.cli_menu.order.select_items")
@patch("src.cli_menu.order.select_courier")
@patch("src.cli_menu.order.ensure_int")
@patch("src.cli_menu.order.typer.prompt")
@patch("src.cli_menu.order.repo_setup")
def test_update_order(
    mock_setup,
    mock_prompt,
    mock_ensure_int,
    mock_select_courier,
    mock_select_items,
    mock_confirm,
    mock_product_repo,
    mock_courier_repo,
    mock_order_repo,
):
    mock_setup.return_value = mock_product_repo, mock_courier_repo, mock_order_repo
    mock_prompt.side_effect = ["Good Patrick", "Patrick's Python Podcast"]
    mock_ensure_int.side_effect = [1, 111111111]
    mock_select_courier.return_value = 2
    mock_select_items.return_value = "2, 1, 2"
    mock_confirm.return_value = False

    with pytest.raises(typer.Abort):
        o.order_update()

    assert mock_order_repo.update.call_args.args == (
        1,
        {
            "customer_name": "Good Patrick",
            "customer_address": "Patrick's Python Podcast",
            "customer_phone": 111111111,
            "courier_id": 2,
            "item_ids": "2, 1, 2",
        },
    )
    assert mock_order_repo.discard.call_count == 1
    assert mock_order_repo.save.call_count == 0


@patch("src.cli_menu.order.confirm")
@patch("src.cli_menu.order.ensure_int")
@patch("src.cli_menu.order.repo_setup")
def test_delete_order(
    mock_setup,
    mock_ensure_int,
    mock_confirm,
    mock_order_repo,
):
    mock_setup.return_value = None, None, mock_order_repo
    mock_ensure_int.return_value = 1
    mock_confirm.return_value = True

    o.order_delete()

    assert mock_order_repo.delete.call_args.args == (1,)
    assert mock_order_repo.save.call_count == 1
    assert mock_order_repo.discard.call_count == 0
