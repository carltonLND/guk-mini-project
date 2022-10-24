#!/usr/bin/env python3
import os

from db.db import create, delete, read, update


def input_int(data=[], menu={}, prompt=">>> "):
    while True:
        try:
            print_menu(menu)
            user_input = int(input(prompt))
        except ValueError:
            os.system("clear")
            print("Invalid Input!\n")
            if data:
                read(data)
        else:
            return user_input


def confirmation(menu):
    confirmation = input_int(menu=menu)
    if confirmation not in menu.keys():
        print("Invalid Input!\n")
        return False

    if confirmation == 0:
        os.system("clear")
        print("Operation Canceled!\n")
        return False

    return True


def print_menu(menu):
    for option, command in menu.items():
        if callable(command):
            command = command.__name__.replace("_", " ").title()

        print(f"{option}) {command}")


def command_loop(data, commands, *args):
    while True:
        command = input_int(menu=commands)
        if command not in commands.keys():
            os.system("clear")
            print("Invalid Input!\n")
            continue

        if command == 0:
            os.system("clear")
            return

        os.system("clear")
        commands[command](data, *args)


def start_application(data, *args):
    menu = args[0]["product_menu"]
    command_loop(data, menu, *args)


def main_menu(data, *args):
    menu = args[0]["main_menu"]
    command_loop(data, menu, *args)


def get_products(data, *_):
    os.system("clear")
    read(data)


def add_product(data, *args):
    os.system("clear")
    new_product = input("Enter Product Name:\n>>> ").strip()
    if not new_product:
        os.system("clear")
        print("Operation Canceled!\n")
        return

    create(data, new_product)
    os.system("clear")
    print(f"New Product: {new_product}!\n")


def update_product(data, *args):
    os.system("clear")
    products_found = read(data)
    if not products_found:
        return

    product_index = input_int(data=data, prompt="Select Product To Update:\n>>> ") - 1
    while product_index > len(data):
        os.system("clear")
        print("Invalid Input!\n")
        read(data)
        product_index = (
            input_int(data=data, prompt="Select Product To Update:\n>>> ") - 1
        )

    os.system("clear")
    new_product_name = input(
        f"Enter New Product Name For '{data[product_index].title()}':\n>>> "
    ).strip()
    print(f"\nUpdate '{data[product_index]}' -> '{new_product_name}'?")
    if not confirmation(args[0]["bool_menu"]):
        return

    os.system("clear")
    print("Product Name Updated!\n")
    update(data, product_index, new_product_name)


def delete_product(data, *args):
    os.system("clear")
    products_found = read(data)
    if not products_found:
        return

    product_index = input_int(data=data, prompt="Select Product To Delete:\n>>> ") - 1
    while product_index > len(data):
        os.system("clear")
        print("Invalid Input!\n")
        read(data)
        product_index = (
            input_int(data=data, prompt="Select Product To Delete:\n>>> ") - 1
        )

    os.system("clear")
    print(f"Delete '{data[product_index]}'?")
    if not confirmation(args[0]["bool_menu"]):
        return

    os.system("clear")
    print("Product Deleted!\n")
    delete(data, product_index)


if __name__ == "__main__":
    MENUS = {
        "main_menu": {1: start_application, 0: "Exit Application"},
        "product_menu": {
            1: get_products,
            2: add_product,
            3: update_product,
            4: delete_product,
            0: main_menu,
        },
        "bool_menu": {1: "Confirm", 0: "Cancel"},
    }

    # Non persistant data
    data = []

    main_menu(data, MENUS)
    print("Exiting Application...")
