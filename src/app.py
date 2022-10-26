#!/usr/bin/env python3
import os

from db.db import create_data, delete_data, get_data, update_data
from file_handlers.txt import format_txt_data


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
            print_data(get_data(data))
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


def manage_products():
    command_loop(MENUS["product_menu"])


def get_products(*_):
    os.system("clear")
    print_data(get_data("products.txt"))


def add_product(*_):
    os.system("clear")
    new_product = input("Enter Product Name:\n>>> ").strip()
    if not new_product:
        os.system("clear")
        return print("Operation Canceled!\n")

    create_data("products.txt", new_product)
    os.system("clear")
    print(f"New Product: {new_product}!\n")


def update_product():
    os.system("clear")
    products = get_data("products.txt")
    if not products:
        return print("No Data Currently Available!\n")

    print_data(products)
    product_index = (
        input_int(data="products.txt", prompt="Select Product To Update:\n>>> ") - 1
    )

    while product_index not in range(len(products)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(products)
        product_index = (
            input_int(data="products.txt", prompt="Select Product To Update:\n>>> ") - 1
        )

    os.system("clear")
    new_product_name = input(
        f"Enter New Product Name For '{products[product_index].title()}':\n>>> "
    ).strip()
    print(f"\nUpdate '{products[product_index]}' -> '{new_product_name}'?")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print("Product Name Updated!\n")
    update_data("products.txt", product_index, new_product_name)


def delete_product():
    os.system("clear")
    products = get_data("products.txt")
    if not products:
        return print("No Data Currently Available!\n")

    print_data(products)
    product_index = (
        input_int(data="products.txt", prompt="Select Product To Delete:\n>>> ") - 1
    )

    while product_index not in range(len(products)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(products)
        product_index = (
            input_int(data="products.txt", prompt="Select Product To Delete:\n>>> ") - 1
        )

    os.system("clear")
    print(f"Delete '{products[product_index]}'?\n")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print("Product Deleted!\n")
    delete_data("products.txt", product_index)


def manage_couriers():
    menu = MENUS["courier_menu"]
    command_loop(menu)


def get_couriers(*_):
    os.system("clear")
    print_data(get_data("couriers.txt"))


def add_courier(*_):
    os.system("clear")
    new_courier = input("Enter Courier Name:\n>>> ").strip()
    if not new_courier:
        os.system("clear")
        return print("Operation Canceled!\n")

    create_data("couriers.txt", new_courier)
    os.system("clear")
    print(f"New Courier: {new_courier}!\n")


def update_courier():
    os.system("clear")
    couriers = get_data("couriers.txt")
    if not couriers:
        return print("No Data Currently Available!\n")

    print_data(couriers)
    courier_index = (
        input_int(data="couriers.txt", prompt="Select Product To Update:\n>>> ") - 1
    )

    while courier_index not in range(len(couriers)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(couriers)
        courier_index = (
            input_int(data="couriers.txt", prompt="Select Product To Update:\n>>> ") - 1
        )

    os.system("clear")
    new_product_name = input(
        f"Enter New Courier Name For '{couriers[courier_index].title()}':\n>>> "
    ).strip()
    print(f"\nUpdate '{couriers[courier_index]}' -> '{new_product_name}'?")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print("Courier Name Updated!\n")
    update_data("couriers.txt", courier_index, new_product_name)


def delete_courier():
    os.system("clear")
    couriers = get_data("couriers.txt")
    if not couriers:
        return print("No Data Currently Available!\n")

    print_data(couriers)
    courier_index = (
        input_int(data="couriers.txt", prompt="Select Product To Delete:\n>>> ") - 1
    )

    while courier_index not in range(len(couriers)):
        os.system("clear")
        print("Invalid Input!\n")
        print_data(couriers)
        courier_index = (
            input_int(data="couriers.txt", prompt="Select Product To Delete:\n>>> ") - 1
        )

    os.system("clear")
    print(f"Delete '{couriers[courier_index]}'?\n")
    if not confirmation(MENUS["bool_menu"]):
        return

    os.system("clear")
    print("Courier Deleted!\n")
    delete_data("couriers.txt", courier_index)


MENUS = {
    "main_menu": {1: manage_products, 2: manage_couriers, 0: "Exit Application"},
    "product_menu": {
        1: get_products,
        2: add_product,
        3: update_product,
        4: delete_product,
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
    format_txt_data()
