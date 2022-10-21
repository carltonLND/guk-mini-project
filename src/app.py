#!/usr/bin/env python3
import os

from db.db import create, delete
from db.db import product_list as data
from db.db import read, update

MAIN_MENU = """1) Start Application
0) Exit Application
>>> """
PRODUCT_MENU = """1) Get Products List
2) Add New Product
3) Update Existing Product (WIP)
4) Delete Product (WIP)
0) Main Menu
>>> """

os.system("clear")
main_menu_input = input(MAIN_MENU)
while main_menu_input != "0":
    if main_menu_input == "1":
        os.system("clear")
        product_menu_input = input(PRODUCT_MENU)
        while product_menu_input != "0":
            if product_menu_input == "1":
                os.system("clear")
                read(data)
                product_menu_input = input(f"\n{PRODUCT_MENU}")

            elif product_menu_input == "2":
                os.system("clear")
                create(data)
                product_menu_input = input(PRODUCT_MENU)

            elif product_menu_input == "3":
                os.system("clear")
                product_found = read(data)
                if not product_found:
                    product_menu_input = input(f"\n{PRODUCT_MENU}")
                    continue

                update(data)
                product_menu_input = input(PRODUCT_MENU)

            elif product_menu_input == "4":
                os.system("clear")
                product_found = read(data)
                if not product_found:
                    product_menu_input = input(f"\n{PRODUCT_MENU}")
                    continue

                delete(data)
                product_menu_input = input(PRODUCT_MENU)

            else:
                os.system("clear")
                print(f"'{product_menu_input}' Is Not A Valid Command!")
                product_menu_input = input(f"\n{PRODUCT_MENU}")

        os.system("clear")

    else:
        os.system("clear")
        print(f"'{main_menu_input}' Is Not A Valid Command!\n")

    main_menu_input = input(MAIN_MENU)

print("\nExiting Application...")
