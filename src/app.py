#!/usr/bin/env python3
import os

from rich.console import Console
from rich.theme import Theme

from db.db import db

console = Console(
    theme=Theme(
        {"base": "#FDF1D6", "notify": "#C39E5C", "warn": "#DA723C", "error": "#EB1D36"}
    )
)


class Menu:
    def __init__(self, options, data_type="") -> None:
        self.options: dict = options
        self.data_type = data_type

    def loop(self):
        while True:
            self.print_menu()
            cmd = self.prompt()
            if cmd == "0":
                os.system("clear")
                break

            if cmd not in self.options.keys():
                os.system("clear")
                console.print("Invalid Option!\n", style="error")
                continue

            os.system("clear")
            self.options[cmd]()

    def print_menu(self):
        for cmd, opt in self.options.items():
            if callable(opt):
                opt = opt.__name__.replace("_", " ").title()

            console.print(f"[notify]{cmd})[/notify] [base]{opt}[/base]")

        if "0" not in self.options.keys():
            console.print(f"[notify]0)[/notify] [base]Return[/base]")

    def get_data(self) -> bool:
        data = db.read(self.data_type)
        if not data:
            console.print("No Data!\n", style="notify")
            return False

        for id, entry in enumerate(data, 1):
            # TODO: print correct data from order dictionary
            if isinstance(entry, dict):
                print("THIS IS A DICT")
            else:
                console.print(f"[notify]{id})[/notify] [base]{entry.name}[/base]")
        else:
            print()
        return True

    @staticmethod
    def prompt():
        return console.input("[notify]>>>[/notify] ")


class MainMenu(Menu):
    def __init__(self) -> None:
        self.options = {
            "1": self.manage_orders,
            "2": self.manage_products,
            "3": self.manage_couriers,
            "0": "Exit",
        }
        self.order_menu = OrderMenu()
        self.product_menu = ProductMenu()
        self.courier_menu = CourierMenu()
        super().__init__(self.options)

    @classmethod
    def run(cls):
        main_menu = cls()
        os.system("clear")
        main_menu.loop()
        os.system("clear")
        console.print("Exiting Application!", style="error")

    def manage_orders(self):
        self.order_menu.loop()

    def manage_products(self):
        self.product_menu.loop()

    def manage_couriers(self):
        self.courier_menu.loop()


class OrderMenu(Menu):
    def __init__(self) -> None:
        self.data_type = "orders"
        self.options = {
            "1": self.get_data,
            "2": self.create_order,
            "3": self.update_status,
            "4": self.update_order,
            "5": self.delete_order,
        }
        super().__init__(self.options, self.data_type)

    def create_order(self):
        pass

    def update_status(self):
        pass

    def update_order(self):
        pass

    def delete_order(self):
        pass


class ProductMenu(Menu):
    def __init__(self) -> None:
        self.data_type = "products"
        self.options = {
            "1": self.get_data,
            "2": self.add_product,
            "3": self.update_product,
            "4": self.delete_product,
        }
        super().__init__(self.options, self.data_type)

    def add_product(self) -> None:
        console.print("Enter New Product Name:", style="base")
        new_product = self.prompt().title()
        db.create_product(name=new_product)
        os.system("clear")
        console.print(f"Product '{new_product}' Added!\n", style="notify")

    def update_product(self) -> None:
        while True:
            if not self.get_data():
                return

            console.print("Enter Product Number To Update:", style="notify")
            try:
                selection = int(self.prompt()) - 1
            except ValueError:
                os.system("clear")
                console.print("Invalid Option!\n", style="error")
                continue

            if selection in range(len(db.products)):
                break

            os.system("clear")
            console.print("Invalid Option!\n", style="error")

        os.system("clear")
        console.print("Enter New Product Name:", style="notify")
        new_name = self.prompt().title()
        db.products[selection].name = new_name
        os.system("clear")
        console.print("Updated Product!\n", style="notify")

    def delete_product(self):
        while True:
            if not self.get_data():
                return

            console.print("Enter Product Number To Delete:", style="notify")
            try:
                selection = int(self.prompt()) - 1
            except ValueError:
                os.system("clear")
                console.print("Invalid Option!\n", style="error")
                continue

            if selection in range(len(db.products)):
                break

            os.system("clear")
            console.print("Invalid Option!\n", style="error")

        os.system("clear")
        db.products.pop(selection)
        os.system("clear")
        console.print("Deleted Product!\n", style="notify")


class CourierMenu(Menu):
    def __init__(self) -> None:
        self.data_type = "couriers"
        self.options = {
            "1": self.get_data,
            "2": self.add_courier,
            "3": self.update_courier,
            "4": self.delete_courier,
        }
        super().__init__(self.options, self.data_type)

    def add_courier(self):
        console.print("Enter New Courier Name:", style="base")
        new_courier = self.prompt().title()
        db.create_courier(name=new_courier)
        os.system("clear")
        console.print(f"Courier '{new_courier}' Added!\n", style="notify")

    def update_courier(self) -> None:
        while True:
            if not self.get_data():
                return

            console.print("Enter Courier Number To Update:", style="notify")
            try:
                selection = int(self.prompt()) - 1
            except ValueError:
                os.system("clear")
                console.print("Invalid Option!\n", style="error")
                continue

            if selection in range(len(db.couriers)):
                break

            os.system("clear")
            console.print("Invalid Option!\n", style="error")

        os.system("clear")
        console.print("Enter New Courier Name:", style="notify")
        new_name = self.prompt().title()
        db.couriers[selection].name = new_name
        os.system("clear")
        console.print("Updated Courier!\n", style="notify")

    def delete_courier(self):
        while True:
            if not self.get_data():
                return

            console.print("Enter Courier Number To Delete:", style="notify")
            try:
                selection = int(self.prompt()) - 1
            except ValueError:
                os.system("clear")
                console.print("Invalid Option!\n", style="error")
                continue

            if selection in range(len(db.couriers)):
                break

            os.system("clear")
            console.print("Invalid Option!\n", style="error")

        os.system("clear")
        db.couriers.pop(selection)
        os.system("clear")
        console.print("Deleted Product!\n", style="notify")


if __name__ == "__main__":
    MainMenu.run()
