#!/usr/bin/env python3
"""CLI menu interface for a pop-up coffee shop management system"""

import typer
from sqlalchemy.orm import sessionmaker

from src.db import couriers_table, orders_table, products_table, setup_lite_db
from src.domain import Courier, Order, Product, SQLProductRepo
from src.utils import *

DATA_PATH = "data/cafe.db"

db = setup_lite_db(DATA_PATH)

Session = sessionmaker(db)

repo = SQLProductRepo(Session())

app = typer.Typer()
product_app = typer.Typer()
courier_app = typer.Typer()
order_app = typer.Typer()

app.add_typer(product_app, name="products", invoke_without_command=True)
app.add_typer(courier_app, name="couriers", invoke_without_command=True)
app.add_typer(order_app, name="orders", invoke_without_command=True)


@product_app.callback()
def product_default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        for product in repo.list(products_table):
            print(f"{product.id}) {product.name}\n - £{product.price:.2f}")


@product_app.command("add")
def product_add():
    name: str = typer.prompt("Name")
    price: float = ensure_float("Price")
    new_product = Product(name=name, price=price)
    repo.add(new_product)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@product_app.command("update")
def product_update():
    product_list = repo.list(products_table)
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    product_choice = ensure_int("Product ID", product_list, default=0)
    if not product_choice:
        raise typer.Abort()

    old_product = repo.get(products_table, product_choice)
    changes = {
        "name": typer.prompt("Name", default=old_product.name, show_default=True),
        "price": ensure_float("Price", default=old_product.price, show_default=True),
    }

    repo.update(products_table, product_choice, changes)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@product_app.command("delete")
def product_delete():
    product_list = repo.list(products_table)
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    product_choice = ensure_int("Product ID", product_list, default=0)
    if not product_choice:
        raise typer.Abort()

    repo.delete(products_table, product_choice)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


#
#
@courier_app.callback()
def courier_default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        for courier in repo.list(couriers_table):
            print(f"{courier.id}) {courier.name}\n - {courier.phone}")


@courier_app.command("add")
def courier_add():
    name: str = typer.prompt("Name")
    phone: int = ensure_int("Phone")
    new_courier = Courier(name=name, phone=phone)
    repo.add(new_courier)
    if not confirm():
        raise typer.Abort()

    repo.save()


@courier_app.command("update")
def courier_update():
    courier_list = repo.list(couriers_table)
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    old_product = repo.get(products_table, courier_choice)
    changes = {
        "name": typer.prompt("Name", default=old_product.name, show_default=True),
        "price": ensure_float("Price", default=old_product.price, show_default=True),
    }

    repo.update(couriers_table, courier_choice, changes)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@courier_app.command("delete")
def courier_delete():
    courier_list = repo.list(couriers_table)
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    repo.delete(couriers_table, courier_choice)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@order_app.callback()
def order_default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        for order in repo.list(orders_table):
            print(f"{order.id}) {order.customer_name}\n - {order.status}")


@order_app.command("add")
def order_add():

    name: str = typer.prompt("Name")
    address: str = typer.prompt("Address")
    phone: int = ensure_int("Phone")
    courier: int = select_courier(repo.list(couriers_table))
    items: str = select_items(repo.list(products_table))

    new_order = Order(
        customer_name=name,
        customer_address=address,
        customer_phone=phone,
        courier_id=courier,
        item_ids=items,
    )

    repo.add(new_order)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@order_app.command("status")
def order_status():
    order_list = repo.list(orders_table)
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.status}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    changes = {"status": select_status()}

    repo.update(orders_table, order_choice, changes)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@order_app.command("update")
def order_update():
    order_list = repo.list(orders_table)
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    old_order = repo.get(orders_table, order_choice)
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
            repo.list(couriers_table), default=old_order.courier_id, show_default=True
        ),
        "item_ids": select_items(
            repo.list(products_table), default=old_order.item_ids, show_default=True
        ),
    }

    repo.update(orders_table, order_choice, changes)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


@order_app.command("delete")
def order_delete():
    order_list = repo.list(orders_table)
    if not order_list:
        print("No orders!")
        raise typer.Abort()

    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")

    order_choice = ensure_int("Order ID", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    repo.delete(orders_table, order_choice)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


if __name__ == "__main__":
    app()
