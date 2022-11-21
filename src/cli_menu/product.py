import typer

from src.db import create_lite_session
from src.domain import Product, SQLRepo
from src.utils import confirm, ensure_float, ensure_int

Session = create_lite_session()

product_repo = SQLRepo(Product, Session())
product_app = typer.Typer()


@product_app.callback(invoke_without_command=True)
def product_default(
    ctx: typer.Context, verbose: bool = typer.Option(False, "--verbose", "-v")
):
    if ctx.invoked_subcommand is not None:
        return

    product_list = product_repo.list()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        if verbose:
            print(
                f"""{product.id}) {product.name}
                \r - {product.price}"""
            )
        else:
            print(f"{product.id}) {product.name}")


@product_app.command("add")
def product_add():
    name: str = typer.prompt("Name")
    price: float = ensure_float("Price")
    new_product = Product(name=name, price=price)
    product_repo.add(new_product)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()


@product_app.command("update")
def product_update():
    product_list = product_repo.list()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    product_choice = ensure_int("Product ID", product_list, default=0)
    if not product_choice:
        raise typer.Abort()

    old_product = product_repo.get(product_choice)
    changes = {
        "name": typer.prompt("Name", default=old_product.name, show_default=True),
        "price": ensure_float("Price", default=old_product.price, show_default=True),
    }

    product_repo.update(product_choice, changes)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()


@product_app.command("delete")
def product_delete():
    product_list = product_repo.list()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    product_choice = ensure_int("Product ID", product_list, default=0)
    if not product_choice:
        raise typer.Abort()

    product_repo.delete(product_choice)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()
