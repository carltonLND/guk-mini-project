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
    if csv:
        setup_csv()
    else:
        setup_db()

    if ctx.invoked_subcommand is not None:
        return

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
def product_add():
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
def product_update():
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
def product_delete():
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


def setup_csv():
    global product_repo

    product_repo = CsvRepo(Product, "products", ["id", "name", "price"])


def setup_db():
    global product_repo

    Session = create_lite_session()
    product_repo = SQLiteRepo(Product, Session())
