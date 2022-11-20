import enum
from dataclasses import dataclass
from enum import Enum

import typer


def ensure_float(prompt: str, default=None) -> float:
    choice = typer.prompt(prompt, default=default, show_default=False)

    if not choice:
        return choice

    try:
        return round(float(choice), 2)
    except ValueError:
        return ensure_float("Invalid price (e.g. 1.50)", default=default)


def ensure_int(prompt: str, options=None, default=None) -> int:
    choice = typer.prompt(prompt, default=default, show_default=False)

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


def update_prompt(data: dict, default=None, choices={}) -> dict:
    new_data = {}
    for key in data.keys():
        if key == "status":
            continue
        if key == "price":
            new_value = ensure_float(f"New {key}", default=default)
        elif key == "items":
            if choices is None or not choices["items"]:
                typer.Exit(1)
            new_value = select_items(choices["items"])
        elif key == "courier":
            if choices is None or not choices["couriers"]:
                typer.Exit(1)
            new_value = select_courier(choices["couriers"])
        else:
            new_value = typer.prompt(f"New {key}", default=default, show_default=False)

        if not new_value:
            continue

        new_data[key] = new_value

    return new_data


def select_courier(choices):
    print(choices)
    print("0) Cancel\n")
    return ensure_int("Courier number", options=choices)


def select_status():
    choices = ("Preparing", "On the way", "Delivered")
    for num, status in enumerate(choices, 1):
        print(f"{num}) {status}")
    print("0) Cancel\n")
    return choices[ensure_int("Select status", options=choices) - 1]


def select_items(choices):
    items = ""
    while True:
        item = str(ensure_int("Product ID", choices, default=""))
        if not item:
            break
        items += f"{item},"

    return items


def confirm() -> bool:
    choice = typer.prompt("Confirm? (Y/n)", default="Y", show_default=False).upper()
    match choice:
        case "Y":
            return True
        case "N":
            return False
        case _:
            return confirm()
