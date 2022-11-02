#!/usr/bin/env python3
import os

from rich.color import parse_rgb_hex
from rich.console import Console
from rich.theme import Theme

from db import db
from menu import CourierMenu, MainMenu, Menu, MenuController, OrderMenu, ProductMenu

console = Console(
    theme=Theme(
        {"base": "#FDF1D6", "notify": "#C39E5C", "warn": "#DA723C", "error": "#EB1D36"}
    )
)


def setup_menu() -> MenuController:
    main_menu = MainMenu()
    return MenuController(
        main_menu=main_menu,
        product_menu=ProductMenu(parent_menu=main_menu),
        courier_menu=CourierMenu(parent_menu=main_menu),
        order_menu=OrderMenu(parent_menu=main_menu),
    )


if __name__ == "__main__":
    ctrl = setup_menu()
    ctrl.print()
    cmd = int(input(">>> "))
    if cmd in range(len(ctrl.current_menu)):
        print(ctrl.current_menu[cmd])
