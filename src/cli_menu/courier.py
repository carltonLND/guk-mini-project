import typer

from src.db import create_lite_session
from src.domain import Courier, CsvRepo, SQLiteRepo
from src.utils import confirm, ensure_float, ensure_int

courier_app = typer.Typer()


@courier_app.callback(invoke_without_command=True)
def courier_default(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Print detailed information of each courier."
    ),
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    if ctx.invoked_subcommand is not None:
        return

    courier_repo = repo_setup(csv)

    courier_list = courier_repo.all()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        if verbose:
            print(
                f"""{courier.id}) Name:  {courier.name}
                \r   Phone: {courier.phone}\n"""
            )
        else:
            print(f"{courier.id}) {courier.name}")


@courier_app.command(
    "add", help="Interactive prompt to add a new courier to the database."
)
def courier_add(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    courier_repo = repo_setup(csv)

    name: str = typer.prompt("Name")
    phone: int = ensure_int("Phone")
    new_courier = Courier(name=name, phone=phone)
    courier_repo.add(new_courier)
    if not confirm():
        raise typer.Abort()

    courier_repo.save()


@courier_app.command(
    "update", help="Interactive prompt to update a courier in the database."
)
def courier_update(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    courier_repo = repo_setup(csv)

    courier_list = courier_repo.all()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    print("0) Cancel")
    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    old_courier = courier_repo.get(courier_choice)
    changes = {
        "name": typer.prompt("Name", default=old_courier.name, show_default=True),
        "phone": ensure_int("Phone", default=old_courier.phone, show_default=True),
    }

    courier_repo.update(courier_choice, changes)
    if not confirm():
        courier_repo.discard()
        raise typer.Abort()

    courier_repo.save()


@courier_app.command(
    "delete", help="Interactive prompt to delete a courier in the database."
)
def courier_delete(
    csv: bool = typer.Option(False, "--csv", help="Work with data in CSV format."),
):
    courier_repo = repo_setup(csv)

    courier_list = courier_repo.all()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    print("0) Cancel")
    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    courier_repo.delete(courier_choice)
    if not confirm():
        courier_repo.discard()
        raise typer.Abort()

    courier_repo.save()


def repo_setup(csv: bool = False):
    if csv:
        return CsvRepo(Courier, "couriers", ["id", "name", "phone"])

    Session = create_lite_session()
    return SQLiteRepo(Courier, Session())
