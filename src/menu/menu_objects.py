from __future__ import annotations

from abc import ABC, abstractmethod

from rich.console import Console
from rich.theme import Theme

default_console = Console(
    theme=Theme(
        {
            "base": "#FDF1D6",
            "prompt": "bold #C36E0C",
            "notify": "#C39E5C",
            "warn": "bold #DA723C",
            "error": "bold #EB1D36",
        }
    ),
    style="base",
    highlight=False,
)


class Menu(ABC):
    name: str
    _parent_menu = None
    _child_menus = ()
    _sibling_menus = {}
    _options = ()

    @abstractmethod
    def run(self):
        pass

    @property
    def sibling_menus(self) -> dict:
        return self._sibling_menus

    @sibling_menus.setter
    def sibling_menus(self, menu: Menu) -> None:
        self._sibling_menus[menu.name] = menu
        menu._sibling_menus[self.name] = self

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

    @staticmethod
    def get_int_input(prompt):
        while True:
            try:
                default_console.print(prompt)
                choice = int(input(">>> "))
            except ValueError:
                default_console.print("[warn]Invalid Input!\n")
            else:
                return choice

    def __len__(self):
        return len(self._options)

    def __getitem__(self, index: int) -> str:
        return self._options[index]

    def __str__(self) -> str:
        menu_options = "**Menu**\n"
        num = 0
        for opt in self._options:
            num += 1
            menu_options += f"{num}) {opt}\n"

        return menu_options.replace(f"{num}", "0")

    def __repr__(self) -> str:
        return self.__class__.__name__


class MenuController:
    def __init__(self, main_menu: Menu, **menus: Menu) -> None:
        self.menus = {"main_menu": main_menu, **menus}
        self.current_menu = main_menu
        self.parent = None

    def populate_siblings(self):
        prev_menu = None
        for name, menu in self.menus.items():
            if name == "main_menu":
                continue

            if prev_menu:
                menu.sibling_menus = prev_menu

            prev_menu = menu

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
            default_console.print("[error]Exiting Application...")
            exit()

        self.current_menu = self.parent
        self.parent = self.current_menu.parent_menu

    def print(self):
        default_console.print(self.current_menu)
