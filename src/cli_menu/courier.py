import typer

from src.db import create_lite_session
from src.domain import Courier, CsvRepo, SQLiteRepo
from src.utils import confirm, ensure_float, ensure_int

courier_app = typer.Typer()


@courier_app.callback(invoke_without_command=True)
def courier_default(
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    csv: bool = typer.Option(False, "--csv"),
):
    if csv:
        setup_csv()
    else:
        setup_db()

    if ctx.invoked_subcommand is not None:
        return

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


@courier_app.command("add")
def courier_add():
    name: str = typer.prompt("Name")
    phone: int = ensure_int("Phone")
    new_courier = Courier(name=name, phone=phone)
    courier_repo.add(new_courier)
    if not confirm():
        raise typer.Abort()

    courier_repo.save()


@courier_app.command("update")
def courier_update():
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


@courier_app.command("delete")
def courier_delete():
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


def setup_csv():
    global courier_repo

    courier_repo = CsvRepo(Courier, "couriers", ["id", "name", "phone"])


def setup_db():
    global courier_repo

    Session = create_lite_session()
    courier_repo = SQLiteRepo(Courier, Session())
