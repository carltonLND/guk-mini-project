from __future__ import annotations

from abc import ABC, abstractmethod


class Menu(ABC):
    _parent_menu = None
    _child_menus = ()
    _options = ()

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


class ProductMenu(Menu):
    def __init__(self, *, parent_menu: Menu) -> None:
        self._options = (
            "Display Products",
            "Add New Product",
            "Update Product",
            "Delete Product",
            "Main Menu",
        )
        self.parent_menu = parent_menu


class CourierMenu(Menu):
    def __init__(self, *, parent_menu: Menu) -> None:
        self._options = (
            "Display Couriers",
            "Add New Courier",
            "Update Courier",
            "Delete Courier",
            "Main Menu",
        )
        self.parent_menu = parent_menu


class OrderMenu(Menu):
    def __init__(self, *, parent_menu: Menu) -> None:
        self._options = (
            "Display Orders",
            "Add New Order",
            "Update Order",
            "Update Status",
            "Delete Order",
            "Main Menu",
        )
        self.parent_menu = parent_menu


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
            return print("Already at the root menu!")

        self.current_menu = self.parent
        self.parent = self.current_menu.parent_menu

    def print(self):
        print(self.current_menu)
