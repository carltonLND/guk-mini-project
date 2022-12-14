import typer

from src.db import create_lite_session
from src.domain import CsvRepo, Product, SQLiteRepo
from src.utils import confirm, ensure_float, ensure_int

product_app = typer.Typer()


@product_app.callback(invoke_without_command=True)
def product_default(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Print detailed information of each product."
    ),
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    if ctx.invoked_subcommand is not None:
        return

    product_repo = repo_setup(csv)

    product_list = product_repo.all()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        if verbose:
            print(
                f"""{product.id}) Name:  {product.name}
            \r   Price: £{product.price:.2f}\n"""
            )
        else:
            print(f"{product.id}) {product.name}")


@product_app.command(
    "add", help="Interactive prompt to add a new product to the database."
)
def product_add(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    product_repo = repo_setup(csv)

    name: str = typer.prompt("Name")
    price: float = ensure_float("Price")
    new_product = Product(name=name, price=price)
    product_repo.add(new_product)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()


@product_app.command(
    "update", help="Interactive prompt to update a product in the database."
)
def product_update(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    product_repo = repo_setup(csv)

    product_list = product_repo.all()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    print("0) Cancel")
    product_choice = ensure_int("Product ID", product_list, default="Q")
    if not product_choice:
        raise typer.Abort()

    old_product = product_repo.get(product_choice)
    if not old_product:
        raise typer.Abort()

    changes = {
        "name": typer.prompt("Name", default=old_product.name, show_default=True),
        "price": ensure_float("Price", default=old_product.price, show_default=True),
    }

    product_repo.update(product_choice, changes)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()


@product_app.command(
    "delete", help="Interactive prompt to delete a product in the database."
)
def product_delete(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    product_repo = repo_setup(csv)

    product_list = product_repo.all()
    if not product_list:
        print("No Products!")
        raise typer.Abort()

    for product in product_list:
        print(f"{product.id}) {product.name}")

    print("0) Cancel")
    product_choice = ensure_int("Product ID", product_list, default=0)
    if not product_choice:
        raise typer.Abort()

    product_repo.delete(product_choice)
    if not confirm():
        product_repo.discard()
        raise typer.Abort()

    product_repo.save()


def repo_setup(csv: bool = False):
    if csv:
        return CsvRepo(Product, "products", ["id", "name", "price"])

    Session = create_lite_session()
    return SQLiteRepo(Product, Session())
