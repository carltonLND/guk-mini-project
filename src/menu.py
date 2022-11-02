from __future__ import annotations

from abc import ABC, abstractmethod

from rich.console import Console
from rich.theme import Theme

from db import db

console = Console(
    theme=Theme(
        {"base": "#FDF1D6", "notify": "#C39E5C", "warn": "#DA723C", "error": "#EB1D36"}
    )
)


class Menu(ABC):
    _parent_menu = None
    _child_menus = ()
    _options = ()

    @abstractmethod
    def run(self):
        pass

    @property
    def child_menus(self) -> tuple:
        return self._child_menus

    @child_menus.setter
    def child_menus(self, menu: Menu) -> None:
        self._child_menus += (menu,)

    @property
    def parent_menu(self) -> Menu | None:
        return self._parent_menu

    @parent_menu.setter
    def parent_menu(self, menu: Menu) -> None:
        menu._child_menus += (self,)
        self._parent_menu = menu

    def __len__(self):
        return len(self._options)

    def __getitem__(self, index: int) -> str:
        return self._options[index]

    def __str__(self) -> str:
        menu_options = ""
        num = 0
        for opt in self._options:
            num += 1
            menu_options += f"{num}) {opt}\n"

        return menu_options.replace(f"{num}", "0")

    def __repr__(self) -> str:
        return self.__class__.__name__


class MainMenu(Menu):
    def __init__(self, *, parent_menu: Menu | None = None) -> None:
        self._options = (
            "Manage Orders",
            "Manage Products",
            "Manage Couriers",
            "Exit Application",
        )

    def run(self, cmd: str = "") -> str | None:
        while True:
            cmd = input(">>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                return "order_menu"
            elif cmd == "2":
                return "product_menu"
            elif cmd == "3":
                return "courier_menu"
            else:
                print("Invalid Input!\n")

            print(self)


class ProductMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.ProductList) -> None:
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
            cmd = input(">>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                print(self.data)
            elif cmd == "2":
                print("Enter Product Name:\n")
                new_product = db.Product(name=input(">>> "))
                self.data.add_data(product=new_product)
                print("Product Added!\n")
            elif cmd == "3":
                print("Not Yet Implemented!\n")
            elif cmd == "4":
                print("Not Yet Implemented!\n")
            else:
                print("Invalid Input!\n")

            print(self)


class CourierMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.CourierList) -> None:
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
            cmd = input(">>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                print(self.data)
            elif cmd == "2":
                print("Enter Product Name:\n")
                new_courier = db.Courier(name=input(">>> ").lower())
                self.data.add_data(courier=new_courier)
                print("Product Added!\n")
            elif cmd == "3":
                print("Not Yet Implemented!\n")
            elif cmd == "4":
                print("Not Yet Implemented!\n")
            else:
                print("Invalid Input!\n")

            print(self)


class OrderMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.OrderList) -> None:
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
            cmd = input(">>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                print(self.data)
            elif cmd == "2":
                print("Enter Client Name:\n")
                name = input(">>> ")
                print("Enter Client Address:\n")
                address = input(">>> ")
                while True:
                    try:
                        print("Enter Client Phone Number:\n")
                        phone = int(input(">>> "))
                    except ValueError:
                        print("Invalid Input!\n")
                    else:
                        break
                new_order = db.Order(name=name, address=address, phone=phone)
                self.data.add_data(order=new_order)
                print("Product Added!\n")
            elif cmd == "3":
                print("Not Yet Implemented!\n")
            elif cmd == "4":
                print("Not Yet Implemented!\n")
            elif cmd == "5":
                print("Not Yet Implemented!\n")
            else:
                print("Invalid Input!\n")

            print(self)


class MenuController:
    def __init__(self, main_menu: Menu, **menus: Menu) -> None:
        self.menus = {"main_menu": main_menu, **menus}
        self.current_menu = main_menu
        self.parent = None

    def next_menu(self, target_menu: str) -> None:
        if target_menu not in self.menus.keys():
            raise SystemExit(
                f"ERROR: Menu '{target_menu}' not added to controller!\nExiting..."
            )

        next_menu = self.menus[target_menu]
        if next_menu not in self.current_menu.child_menus:
            raise SystemExit(
                f"ERROR: '{target_menu}' is not a valid child menu!\nExiting..."
            )

        self.parent = self.current_menu
        self.current_menu = self.menus[target_menu]

    def prev_menu(self) -> None:
        if not self.parent:
            raise SystemExit("Exiting Application...")

        self.current_menu = self.parent
        self.parent = self.current_menu.parent_menu

    def print(self):
        print(self.current_menu)

    @classmethod
    def setup_factory(cls) -> MenuController:
        product_data = db.ProductList()
        courier_data = db.CourierList()
        order_data = db.OrderList()
        main_menu = MainMenu()
        return cls(
            main_menu=main_menu,
            product_menu=ProductMenu(parent_menu=main_menu, data=product_data),
            courier_menu=CourierMenu(parent_menu=main_menu, data=courier_data),
            order_menu=OrderMenu(parent_menu=main_menu, data=order_data),
        )
