import typer

from src.db import create_lite_session
from src.domain import Courier, Order, Product, SQLRepo
from src.utils import (confirm, ensure_int, select_courier, select_items,
                       select_status)

Session = create_lite_session()

product_repo = SQLRepo(Product, Session())
courier_repo = SQLRepo(Courier, Session())
order_repo = SQLRepo(Order, Session())

order_app = typer.Typer()


@order_app.callback(invoke_without_command=True)
def order_default(
    ctx: typer.Context, verbose: bool = typer.Option(False, "--verbose", "-v")
):
    if ctx.invoked_subcommand is not None:
        return

    order_list = order_repo.all()
    if not order_list:
        print("No Orders!")
        raise typer.Abort()

    for order in order_list:
        if verbose:
            print(
                f"""{order.id}) Name:    {order.customer_name}
                \r   Address: {order.customer_address}
                \r   Phone:   {order.customer_phone}
                \r   Courier: {order.courier_id}
                \r   Items:   {order.item_ids}
                \r   Status:  {order.status}\n"""
            )
        else:
            print(f"{order.id}) {order.customer_name}\n - {order.status}")


@order_app.command("add")
def order_add():
    courier_list = courier_repo.all()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    product_list = product_repo.all()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    name: str = typer.prompt("Name")
    address: str = typer.prompt("Address")
    phone: int = ensure_int("Phone")
    courier: int = select_courier(courier_list)
    items: str = select_items(product_list)

    new_order = Order(
        customer_name=name,
        customer_address=address,
        customer_phone=phone,
        courier_id=courier,
        item_ids=items,
    )

    order_repo.add(new_order)
    if not confirm():
        order_repo.discard()
        raise typer.Abort()

    order_repo.save()


@order_app.command("status")
def order_status():
    order_list = order_repo.all()
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.status}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    changes = {"status": select_status()}

    order_repo.update(order_choice, changes)
    if not confirm():
        order_repo.discard()
        raise typer.Abort()

    order_repo.save()


@order_app.command("update")
def order_update():
    order_list = order_repo.all()
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    old_order = order_repo.get(order_choice)
    changes = {
        "customer_name": typer.prompt(
            "Name", default=old_order.customer_name, show_default=True
        ),
        "customer_address": typer.prompt(
            "Address", default=old_order.customer_address, show_default=True
        ),
        "customer_phone": ensure_int(
            "Phone", default=old_order.customer_phone, show_default=True
        ),
        "courier_id": select_courier(
            courier_repo.all(), default=old_order.courier_id, show_default=True
        ),
        "item_ids": select_items(
            product_repo.all(), default=old_order.item_ids, show_default=True
        ),
    }

    order_repo.update(order_choice, changes)
    if not confirm():
        order_repo.discard()
        raise typer.Abort()

    order_repo.save()


@order_app.command("delete")
def order_delete():
    order_list = order_repo.all()
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    order_repo.delete(order_choice)
    if not confirm():
        order_repo.discard()
        raise typer.Abort()

    order_repo.save()
