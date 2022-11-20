#!/usr/bin/env python3
"""CLI menu interface for a pop-up coffee shop management system"""

import typer
from sqlalchemy.orm import sessionmaker

from src.db import couriers_table, orders_table, products_table, setup_lite_db
from src.domain import Courier, Order, Product, Repository
from src.utils import *

DATA_PATH = "data/cafe.db"

db = setup_lite_db(DATA_PATH)

Session = sessionmaker(db)

repo = Repository(Session())

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


# @product_app.command("update")
# def product_update():
#     print(data_controller.products)
#     print("0) Cancel\n")
#     product_choice = ensure_int("Product number", options=data_controller.products)
#     if not product_choice:
#         raise typer.Abort()
#
#     product = data_controller.products.get(product_choice - 1)
#     new_product = update_prompt(product.__dict__, default="")
#     product.update(**new_product)
#     if not confirm():
#         raise typer.Abort()
#
#     data_controller.save()
#
#
@product_app.command("delete")
def product_delete():
    product_list = repo.list(products_table)
    for product in product_list:
        print(f"{product.id}) {product.name}")

    product_choice = ensure_int("Product id", product_list, default=0)
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


#
#
# @courier_app.command("update")
# def courier_update():
#     print(data_controller.couriers)
#     print("0) Cancel\n")
#     courier_choice = ensure_int("Courier number", options=data_controller.couriers)
#     if not courier_choice:
#         raise typer.Abort()
#
#     courier = data_controller.couriers.get(courier_choice - 1)
#     new_courier = update_prompt(courier.__dict__, default="")
#     courier.update(**new_courier)
#     if not confirm():
#         raise typer.Abort()
#
#     data_controller.save()


@courier_app.command("delete")
def courier_delete():
    courier_list = repo.list(couriers_table)
    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    courier_choice = ensure_int("Courier id", courier_list, default=0)
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
            print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")


@order_app.command("add")
def order_add():
    name: str = typer.prompt("Name")
    address: str = typer.prompt("Address")
    phone: int = ensure_int("Phone")

    couriers = repo.list(couriers_table)
    print(couriers)
    courier = ensure_int("Courier ID", couriers)
    if not courier:
        raise typer.Abort()

    products = repo.list(products_table)
    print(products)
    items = select_items(products)
    if not items:
        raise typer.Abort()

    new_order = Order(
        customer_name=name,
        customer_address=address,
        customer_phone=phone,
        courier_id=courier,
        item_ids=items.rstrip(","),
    )

    repo.add(new_order)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


#
#
# @order_app.command("status")
# def order_status():
#     print(data_controller.orders)
#     print("0) Cancel\n")
#     order_choice = ensure_int("Order number", options=data_controller.orders)
#     if not order_choice:
#         raise typer.Abort()
#
#     order = data_controller.orders.get(order_choice - 1)
#     new_order = {}
#     new_order["status"] = select_status()
#     order.update(**new_order)
#     if not new_order["status"]:
#         raise typer.Abort()
#
#     data_controller.save()
#
#
# @order_app.command("update")
# def order_update():
#     print(data_controller.orders)
#     print("0) Cancel\n")
#     order_choice = ensure_int("Order number", options=data_controller.orders)
#     if not order_choice:
#         raise typer.Abort()
#
#     order = data_controller.orders.get(order_choice - 1)
#     new_order = update_prompt(
#         order.__dict__,
#         default="",
#         choices={
#             "items": data_controller.products,
#             "couriers": data_controller.couriers,
#         },
#     )
#
#     order.update(**new_order)
#     if not confirm():
#         raise typer.Abort()
#
#     data_controller.save()


@order_app.command("delete")
def order_delete():
    order_list = repo.list(orders_table)
    for order in order_list:
        print(f"{order.id}) {order.customer_name}\n - {order.item_ids}")

    order_choice = ensure_int("Order id", order_list, default=0)
    if not order_choice:
        raise typer.Abort()

    repo.delete(orders_table, order_choice)
    if not confirm():
        repo.discard()
        raise typer.Abort()

    repo.save()


if __name__ == "__main__":
    # data_controller.load()
    app()
