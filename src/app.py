#!/usr/bin/env python3
import os

from db.db import products_list as data

MAIN_MENU = """1) Start Application
0) Exit Application
>>> """
PRODUCT_MENU = """1) Get Products List
\r2) Add New Product
\r3) Update Existing Product (WIP)
\r4) Delete Product (WIP)
\r0) Main Menu
\r>>> """

os.system("clear")
main_menu_input = input(MAIN_MENU)
while main_menu_input != "0":
    if main_menu_input == "1":
        os.system("clear")
        product_menu_input = input(PRODUCT_MENU)
        while product_menu_input != "0":
            if product_menu_input == "1":
                os.system("clear")
                if not data:
                    print("No Products Currently Available!")
                else:
                    print("Products:")
                    for index, product in enumerate(data, 1):
                        print(f"{index}) {product.title()}")

                product_menu_input = input(f"\n{PRODUCT_MENU}")

            elif product_menu_input == "2":
                os.system("clear")
                new_product = input("Enter Product Name:\n>>> ").strip()
                data.append(new_product)
                os.system("clear")
                print(f"New Product #{len(data)}: {new_product}!\n")
                product_menu_input = input(PRODUCT_MENU)

            elif product_menu_input == "3":
                #         # STRETCH GOAL - UPDATE existing product
                #         PRINT product names with its index value
                #         GET user input for product index value
                #         GET user input for new product name
                #         UPDATE product name at index in products list
                pass

            elif product_menu_input == "4":
                #         # STRETCH GOAL - DELETE product
                #         PRINT products list
                #         GET user input for product index value
                #         DELETE product at index in products list
                pass
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
