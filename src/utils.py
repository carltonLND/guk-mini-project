import typer


def ensure_float(prompt: str, default=None, show_default=False) -> float:
    choice = typer.prompt(prompt, default=default, show_default=show_default)

    if not choice:
        return choice

    try:
        return round(float(choice), 2)
    except ValueError:
        return ensure_float("Invalid price (e.g. 1.50)", default=default)


def ensure_int(prompt: str, options=None, default=None, show_default=False) -> int:
    choice = typer.prompt(prompt, default=default, show_default=show_default)

    if not choice:
        return choice

    try:
        choice = int(choice)
    except ValueError:
        return ensure_int(prompt, options=options, default=default)

    if not options:
        return choice

    if choice not in range(0, len(options) + 1):
        return ensure_int(prompt, options=options, default=default)

    return choice


def select_status():
    choices = ("Preparing", "On the way", "Delivered")
    for num, status in enumerate(choices, 1):
        print(f"{num}) {status}")
    print("0) Cancel")
    return choices[ensure_int("Select status", options=choices) - 1]


def select_courier(choices, default=None, show_default=False):
    for choice in choices:
        print(f"{choice.id}) {choice.name}")
    print("0) Cancel")
    courier = ensure_int(
        "Courier ID", choices, default=default, show_default=show_default
    )
    if not courier:
        raise typer.Abort()

    return courier


def select_items(choices, default="", show_default=False):
    for choice in choices:
        print(f"{choice.id}) {choice.name}\n - £{choice.price:.2f}")
    print("0) Done")
    items = ""
    while True:
        item = ensure_int(
            "Product ID", choices, default=default, show_default=show_default
        )
        if not item:
            break
        items += f"{item},"

    if not items:
        raise typer.Abort()

    return items.rstrip(",")


def confirm() -> bool:
    choice = typer.prompt("Confirm? (Y/n)", default="Y", show_default=False).upper()
    match choice:
        case "Y":
            return True
        case "N":
            return False
        case _:
            return confirm()
