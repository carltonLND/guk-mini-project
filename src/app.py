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
    def __init__(self, options) -> None:
        self.options: dict = options

    def loop(self):
        while True:
            self.print_menu()
            cmd = self.prompt()
            if cmd == "0":
                os.system("clear")
                break

            if cmd not in self.options.keys():
                os.system("clear")
                console.print("Invalid Option!\n", style="warn")
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
        self.options = {
            "1": self.get_orders,
            "2": self.create_order,
            "3": self.update_status,
            "4": self.update_order,
            "5": self.delete_order,
        }
        super().__init__(self.options)

    def get_orders(self):
        pass

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
        self.options = {
            "1": self.get_products,
            "2": self.add_product,
            "3": self.update_product,
            "4": self.delete_product,
        }
        super().__init__(self.options)

    def get_products(self) -> None:
        products = db.read("products")
        if not products:
            return console.print("No Products!\n", style="notify")

        for id, entry in enumerate(products, 1):
            console.print(f"[notify]{id})[/notify] [base]{entry.name}[/base]")
        else:
            print()

    def add_product(self):
        console.print("Enter New Product Name:", style="base")
        new_product = self.prompt().title()
        db.create_product(name=new_product)
        os.system("clear")
        console.print(f"Product '{new_product}' Added!\n", style="notify")

    def update_product(self):
        pass

    def delete_product(self):
        pass


class CourierMenu(Menu):
    def __init__(self) -> None:
        self.options = {
            "1": self.get_couriers,
            "2": self.add_courier,
            "3": self.update_courier,
            "4": self.delete_courier,
        }
        super().__init__(self.options)

    def get_couriers(self) -> None:
        couriers = db.read("couriers")
        if not couriers:
            return console.print("No Couriers!\n", style="notify")

        for id, entry in enumerate(couriers, 1):
            console.print(f"[notify]{id})[/notify] [base]{entry.name}[/base]")
        else:
            print()

    def add_courier(self):
        console.print("Enter New Courier Name:", style="base")
        new_courier = self.prompt().title()
        db.create_courier(name=new_courier)
        os.system("clear")
        console.print(f"Courier '{new_courier}' Added!\n", style="notify")

    def update_courier(self):
        pass

    def delete_courier(self):
        pass


if __name__ == "__main__":
    MainMenu.run()
