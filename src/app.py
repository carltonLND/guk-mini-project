#!/usr/bin/env python3
import os

from db.db import create, delete, read, update


def print_menu(menu):
    prompt = ">>> "
    for option, message in menu.items():
        print(f"{option}) {message}")

    return input(prompt)


def product_menu_loop(data, product_menu, bool_menu):
    user_input = print_menu(product_menu)
    while user_input != "0":
        # Print list of products
        if user_input == "1":
            os.system("clear")
            read(data)
            user_input = print_menu(product_menu)

        # Add new product to db
        elif user_input == "2":
            os.system("clear")
            new_product = input("Enter Product Name:\n>>> ").strip()
            if not new_product:
                os.system("clear")
                print("Operation Canceled!\n")
                user_input = print_menu(product_menu)
                continue

            create(data, new_product)
            os.system("clear")
            print(f"New Product: {new_product}!\n")
            user_input = print_menu(product_menu)

        # Update existing product
        elif user_input == "3":
            os.system("clear")
            product_found = read(data)
            if not product_found:
                os.system("clear")
                print("Operation Canceled!\n")
                user_input = print_menu(product_menu)
                continue

            try:
                product_index = int(input("Select Product To Update:\n>>> ")) - 1
                new_product_name = input(f"\nEnter New Product Name:\n>>> ").strip()
                print(f"\nUpdate '{data[product_index]}' -> '{new_product_name}'?")
                confirmation = print_menu(bool_menu)
                if confirmation == "0":
                    os.system("clear")
                    print("Operation Canceled!\n")
                    continue

                if confirmation == "1":
                    os.system("clear")
                    print("Product Name Updated!\n")
                    update(data, product_index, new_product_name)

            except ValueError:
                os.system("clear")
                print("Invalid Input!\n")
            except IndexError:
                os.system("clear")
                print("Invalid Input!\n")
            finally:
                user_input = print_menu(product_menu)

        # Delete product from db
        elif user_input == "4":
            os.system("clear")
            product_found = read(data)
            if not product_found:
                user_input = print_menu(product_menu)
                continue

            try:
                product_index = int(input("\nSelect Product To Delete:\n>>> ")) - 1
                print(f"Delete '{data[product_index]}'?\n")
                confirmation = print_menu(bool_menu)
                if confirmation == "0":
                    os.system("clear")
                    print("Operation Canceled!\n")
                    continue

                if confirmation == "1":
                    os.system("clear")
                    print("Product Deleted!\n")
                    delete(data, product_index)

            except ValueError:
                os.system("clear")
                print("Invalid Input!\n")
            except IndexError:
                os.system("clear")
                print("Invalid Input!\n")
            finally:
                user_input = print_menu(product_menu)

        else:
            os.system("clear")
            print(f"'{user_input}' Is Not A Valid Command!\n")
            user_input = print_menu(product_menu)

    os.system("clear")


def main_menu_loop(data, main_menu, product_menu, bool_menu):
    os.system("clear")
    user_input = print_menu(main_menu)
    while user_input != "0":
        if user_input == "1":
            os.system("clear")
            product_menu_loop(data, product_menu, bool_menu)

        else:
            os.system("clear")
            print(f"'{user_input}' Is Not A Valid Command!\n")

        user_input = print_menu(main_menu)


if __name__ == "__main__":
    MAIN_MENU = {1: "Start Application", 0: "Exit Application"}
    PRODUCT_MENU = {
        1: "Get Products List",
        2: "Add New Product",
        3: "Update Existing Product",
        4: "Delete Product",
        0: "Main Menu",
    }
    BOOL_MENU = {1: "Yes", 0: "No"}

    # Non persistant data
    data = []

    main_menu_loop(data, MAIN_MENU, PRODUCT_MENU, BOOL_MENU)
    print("\nExiting Application...")
