#!/usr/bin/env python3
import os
from enum import Enum, auto
from pathlib import Path

import db
from file_handlers import Handler, TXTHandler
from menu import Menu, MenuController
from menu import default_console as console


class FileType(Enum):
    TXT = auto()


class MainMenu(Menu):
    def __init__(self) -> None:
        self.name = "main_menu"
        self._options = (
            "Manage Orders",
            "Manage Products",
            "Manage Couriers",
            "Exit Application",
        )

    def run(self, cmd: str = "") -> str | None:
        while True:
            console.print(self)
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                return "order_menu"
            elif cmd == "2":
                return "product_menu"
            elif cmd == "3":
                return "courier_menu"
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")


class ProductMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.ProductList) -> None:
        self.name = "product_menu"
        self._options = (
            "Display Products",
            "Add New Product",
            "Update Product",
            "Delete Product",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            console.print(self)
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                self.add_product()
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")

    def add_product(self):
        console.print("[notify]Enter Product Name:\n")
        new_product = db.Product(name=console.input("[prompt]>>> "))
        self.data.add_data(data=new_product)
        console.clear()
        console.print("[notify]Product Added!\n")


class CourierMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.CourierList) -> None:
        self.name = "courier_menu"
        self._options = (
            "Display Couriers",
            "Add New Courier",
            "Update Courier",
            "Delete Courier",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            console.print(self)
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                console.print("Enter Courier Name:\n")
                new_courier = db.Courier(name=input(">>> ").lower())
                self.data.add_data(data=new_courier)
                console.clear()
                console.print("Courier Added!\n")
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")


class OrderMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.OrderList) -> None:
        self.name = "order_menu"
        self._options = (
            "Display Orders",
            "Add New Order",
            "Update Order",
            "Update Status",
            "Delete Order",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            console.print(self)
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                console.clear()
                if not self.sibling_menus["courier_menu"].data.data_exists():
                    console.print("No Couriers Available\n")
                    continue

                console.print("Enter Client Name:\n")
                name = input(">>> ")

                console.print("Enter Client Address:\n")
                address = input(">>> ")

                phone = self.get_int_input("Enter Client Phone Number:\n")

                courier_data = self.sibling_menus["courier_menu"].data
                console.print(courier_data)
                courier = self.get_int_input("Select Courier By Number:\n")
                while courier not in range(1, len(courier_data) + 1):
                    console.print("Invalid Input!\n")
                    console.print(courier_data)
                    courier = self.get_int_input("Select Courier By Number:\n")

                new_order = db.Order(
                    name=name, address=address, phone=phone, courier=courier
                )
                self.data.add_data(data=new_order)
                console.clear()
                console.print("Order Added!\n")
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "5":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")


def handler_factory(file_type: FileType) -> Handler:
    data_dir = os.path.join(Path(__file__).parent.parent, "data/")
    match file_type:
        case FileType.TXT:
            return TXTHandler(data_dir)
        case _:
            raise TypeError("Filetype not currently supported")


def data_factory(handler) -> dict:
    courier_data = db.CourierList(file_handler=handler)
    product_data = db.ProductList(file_handler=handler)
    order_data = db.OrderList(file_handler=handler)
    return {"products": product_data, "couriers": courier_data, "orders": order_data}


def cafe_factory() -> MenuController:
    handler = handler_factory(FileType.TXT)
    data = data_factory(handler)

    main_menu = MainMenu()
    product_menu = ProductMenu(parent_menu=main_menu, data=data["products"])
    courier_menu = CourierMenu(parent_menu=main_menu, data=data["couriers"])
    order_menu = OrderMenu(parent_menu=main_menu, data=data["orders"])

    controller = MenuController(
        main_menu=main_menu,
        product_menu=product_menu,
        courier_menu=courier_menu,
        order_menu=order_menu,
    )

    controller.populate_siblings()
    return controller


def main() -> None:
    with console.status("[warn]Loading Data..."):
        controller = cafe_factory()

    while True:
        console.clear()
        menu = controller.current_menu.run()
        if not menu:
            controller.prev_menu()
        else:
            controller.next_menu(menu)


if __name__ == "__main__":
    main()
