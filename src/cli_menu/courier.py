import typer

from src.db import create_lite_session
from src.domain import Courier, SQLRepo
from src.utils import confirm, ensure_float, ensure_int

Session = create_lite_session()

courier_repo = SQLRepo(Courier, Session())
courier_app = typer.Typer()


@courier_app.callback(invoke_without_command=True)
def courier_default(
    ctx: typer.Context, verbose: bool = typer.Option(False, "--verbose", "-v")
):
    if ctx.invoked_subcommand is not None:
        return

    courier_list = courier_repo.list()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        if verbose:
            print(
                f"""{courier.id}) {courier.name}
                \r - {courier.phone}"""
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
    courier_list = courier_repo.list()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    old_courier = courier_repo.get(courier_choice)
    changes = {
        "name": typer.prompt("Name", default=old_courier.name, show_default=True),
        "phone": ensure_float("Phone", default=old_courier.phone, show_default=True),
    }

    courier_repo.update(courier_choice, changes)
    if not confirm():
        courier_repo.discard()
        raise typer.Abort()

    courier_repo.save()


@courier_app.command("delete")
def courier_delete():
    courier_list = courier_repo.list()
    if not courier_list:
        print("No Couriers!")
        raise typer.Abort()

    for courier in courier_list:
        print(f"{courier.id}) {courier.name}")

    courier_choice = ensure_int("Courier ID", courier_list, default=0)
    if not courier_choice:
        raise typer.Abort()

    courier_repo.delete(courier_choice)
    if not confirm():
        courier_repo.discard()
        raise typer.Abort()

    courier_repo.save()
