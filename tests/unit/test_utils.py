from unittest.mock import patch

import pytest
import typer

import src.utils as u
from src.domain import Courier, Product


@pytest.fixture
def product_fixture():
    return Product(id=1, name="Coffee", price=1.10)


@pytest.fixture
def courier_fixture():
    return Courier(id=1, name="Coffee", phone=11111)


@patch("src.utils.typer.prompt")
def test_ensure_float(mock_prompt):
    mock_prompt.return_value = "10.55"

    assert u.ensure_float("Enter Float") == 10.55


@patch("src.utils.typer.prompt")
def test_bad_ensure_float(mock_prompt):
    mock_prompt.side_effect = ["ten point five five", 10.55]

    assert u.ensure_float("Enter Float") == 10.55
    assert mock_prompt.call_count == 2


@patch("src.utils.typer.prompt")
def test_bad_ensure_float_recursion(mock_prompt):
    mock_prompt.return_value = "ten point five five"

    with pytest.raises(RecursionError):
        u.ensure_float("Enter Float")


@patch("src.utils.typer.prompt")
def test_ensure_int(mock_prompt):
    mock_prompt.return_value = 3

    assert u.ensure_int("Enter Int") == 3


@patch("src.utils.typer.prompt")
def test_bad_ensure_int(mock_prompt):
    mock_prompt.side_effect = ["abc", "five", 5]

    assert u.ensure_int("Enter Int") == 5
    assert mock_prompt.call_count == 3


@patch("src.utils.typer.prompt")
def test_ensure_int_in_options(mock_prompt):
    mock_prompt.return_value = 1
    fake_options = [{"id": 1}]

    assert u.ensure_int("Enter Int", options=fake_options) == 1


@patch("src.utils.typer.prompt")
def test_ensure_int_not_in_options(mock_prompt, product_fixture):
    mock_prompt.return_value = 190284
    fake_options = [product_fixture]

    with pytest.raises(RecursionError):
        u.ensure_int("Enter Int", options=fake_options)


@patch("src.utils.typer.prompt")
def test_ensure_int_in_options_attempts(mock_prompt, product_fixture):
    mock_prompt.side_effect = [190284, 3, 1]
    fake_options = [product_fixture]

    assert u.ensure_int("Enter Int", options=fake_options) == 1
    assert mock_prompt.call_count == 3


@patch("src.utils.ensure_int")
def test_select_valid_status(mock_ensure_int):
    mock_ensure_int.return_value = 2

    assert u.select_status() == "2 (On the way)"


@patch("src.utils.ensure_int")
def test_cancel_select_status(mock_ensure_int):
    mock_ensure_int.return_value = 0

    with pytest.raises(typer.Abort):
        u.select_status()


@patch("src.utils.ensure_int")
def test_select_courier(mock_ensure_int, courier_fixture):
    mock_ensure_int.return_value = 1
    fake_options = [courier_fixture]

    assert u.select_courier(fake_options) == 1


@patch("src.utils.ensure_int")
def test_cancel_select_courier(mock_ensure_int, courier_fixture):
    mock_ensure_int.return_value = 0
    fake_options = [courier_fixture]

    with pytest.raises(typer.Abort):
        u.select_courier(fake_options)


@patch("src.utils.ensure_int")
def test_select_items(mock_ensure_int, product_fixture):
    mock_ensure_int.side_effect = 1, 1, 1, 0
    fake_options = [product_fixture]

    assert u.select_items(fake_options) == "1,1,1"


@patch("src.utils.ensure_int")
def test_select_no_items(mock_ensure_int, product_fixture):
    mock_ensure_int.return_value = 0
    fake_options = [product_fixture]

    with pytest.raises(typer.Abort):
        u.select_items(fake_options)


@patch("src.utils.typer.prompt")
def test_confirm(mock_prompt):
    mock_prompt.return_value = "Y"

    assert u.confirm() == True


@patch("src.utils.typer.prompt")
def test_confirm_lower_case(mock_prompt):
    mock_prompt.return_value = "y"

    assert u.confirm() == True


@patch("src.utils.typer.prompt")
def test_no_confirm(mock_prompt):
    mock_prompt.return_value = "N"

    assert u.confirm() == False


@patch("src.utils.typer.prompt")
def test_no_confirm_lower_case(mock_prompt):
    mock_prompt.return_value = "n"

    assert u.confirm() == False


@patch("src.utils.typer.prompt")
def test_bad_confirm_recursion(mock_prompt):
    mock_prompt.side_effect = ["1", "2", "3", "a", "Y"]

    assert u.confirm() == True
    assert mock_prompt.call_count == 5
