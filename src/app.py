#!/usr/bin/env python3
import os

from db import db


def create_data_display(data_file, data="Data"):
    os.system("clear")
    item = input(f"Enter {data} Name:\n>>> ").strip()
    if not item:
        os.system("clear")
        return print("Operation Canceled!\n")

    db.create_data(data_file, item)
    os.system("clear")
    print(f"New {data}: {item}!\n")


def create_multi_data_display(prompts, data_file, data="Data", **kwargs):
    os.system("clear")
    items = {}
    for prompt in prompts:
        items[prompt] = input(f"Enter Your {prompt}:\n>>> ")

    if not items:
        os.system("clear")
        return print("Operation Canceled!\n")

    for key, value in kwargs.items():
        items[key] = value

    db.create_data(data_file, items, multi=True)
    os.system("clear")
    print(f"{data} Added!\n")


def update_data_display(data_file, data="Data"):
    os.system("clear")
    items = db.get_data(data_file)
    if not items:
        return print("No Data Currently Available!\n")

    print_data(items)
    item_index = input_int(data=data_file, prompt=f"Select {data} To Update:\n>>> ") - 1
    while item_index not in range(len(items)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(items)
        item_index = (
            input_int(data=data_file, prompt=f"Select {data} To Update:\n>>> ") - 1
        )

    os.system("clear")
    new_item = input(
        f"Enter New {data} Name For '{items[item_index].title()}':\n>>> "
    ).strip()
    print(f"\nUpdate '{items[item_index]}' -> '{new_item}'?")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print(f"{data} Name Updated!\n")
    db.update_data(data_file, item_index, new_item)


def delete_data_display(data_file, data="Data"):
    os.system("clear")
    items = db.get_data(data_file)
    if not items:
        return print("No Data Currently Available!\n")

    print_data(items)
    item_index = input_int(data=data_file, prompt=f"Select {data} To Delete:\n>>> ") - 1
    while item_index not in range(len(items)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(items)
        item_index = (
            input_int(data=data_file, prompt=f"Select {data} To Delete:\n>>> ") - 1
        )

    os.system("clear")
    print(f"Delete '{items[item_index]}'?\n")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print(f"{data} Deleted!\n")
    db.delete_data(data_file, item_index)


def main_menu():
    os.system("clear")
    command_loop(MENUS["main_menu"])


def command_loop(menu):
    while True:
        command = input_int(menu=menu)
        if command not in menu.keys():
            os.system("clear")
            print("Invalid Input!\n")
            continue

        if command == 0:
            return os.system("clear")

        os.system("clear")
        menu[command]()


def print_menu(menu):
    for option, command in menu.items():
        if callable(command):
            command = command.__name__.replace("_", " ").title()

        print(f"{option}) {command}")


def print_data(data):
    if not data:
        return print("No Data Currently Available!\n")
    print("Data:")
    for id, data in enumerate(data, 1):
        print(f"{id}) {data.title()}")
    print()


def input_int(data="", menu={}, prompt=">>> "):
    while True:
        try:
            print_menu(menu)
            user_input = int(input(prompt))
        except ValueError:
            os.system("clear")
            print("Invalid Input!\n")
            if not data:
                continue
            print_data(db.get_data(data))
        else:
            return user_input


def confirmation(menu):
    confirmation = input_int(menu=menu)
    if confirmation not in menu.keys():
        os.system("clear")
        print("Invalid Input!\n")
        return False

    if confirmation == 0:
        os.system("clear")
        print("Operation Canceled!\n")
        return False

    return True


def manage_orders():
    command_loop((MENUS["order_menu"]))


def get_orders(*_):
    os.system("clear")
    print_data(db.get_data("orders.txt", multi=True))


def create_order(*_):
    prompts = ["Name", "Address", "Phone"]
    create_multi_data_display(prompts, "orders.txt", data="Order", status="Preparing")


def update_order_status():
    pass


def update_order_details():
    pass


def delete_order():
    pass


def manage_products():
    command_loop(MENUS["product_menu"])


def get_products(*_):
    os.system("clear")
    print_data(db.get_data("products.txt"))


def add_product(*_):
    create_data_display("products.txt", data="Product")


def update_product():
    update_data_display("products.txt", data="Product")


def delete_product():
    delete_data_display("products.txt", data="Product")


def manage_couriers():
    menu = MENUS["courier_menu"]
    command_loop(menu)


def get_couriers(*_):
    os.system("clear")
    print_data(db.get_data("couriers.txt"))


def add_courier(*_):
    create_data_display("couriers.txt", data="Courier")


def update_courier():
    update_data_display("couriers.txt", data="Courier")


def delete_courier():
    delete_data_display("couriers.txt", data="Courier")


MENUS = {
    "main_menu": {
        1: manage_orders,
        2: manage_products,
        3: manage_couriers,
        0: "Exit Application",
    },
    "product_menu": {
        1: get_products,
        2: add_product,
        3: update_product,
        4: delete_product,
        0: main_menu,
    },
    "order_menu": {
        1: get_orders,
        2: create_order,
        3: update_order_status,
        4: update_order_details,
        5: delete_order,
        0: main_menu,
    },
    "courier_menu": {
        1: get_couriers,
        2: add_courier,
        3: update_courier,
        4: delete_courier,
        0: main_menu,
    },
    "bool_menu": {1: "Confirm", 0: "Cancel"},
}


if __name__ == "__main__":
    main_menu()
    print("Exiting Application...")
