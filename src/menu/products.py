from db import ABCDataController

from .menu import Menu


class ProductMenu(Menu):
    """Menu for interfacing with products"""

    _OPTIONS = (
        "Display Products",
        "Add New Product",
        "Update Existing Product",
        "Delete Product",
        "Return",
    )

    def __init__(self, data_controller: ABCDataController) -> None:
        self.commands = {
            1: self.print_products,
            2: self.add_product,
            3: self.update_product,
            4: self.delete_product,
            0: self.exit_menu,
        }
        super().__init__(data_controller)

    def print_products(self) -> bool:
        print(self.data_controller.products)
        return True

    def add_product(self) -> bool:
        new_product = {}
        new_product["name"] = input("Product name:\n\n>>> ")
        new_product["price"] = float(input("Product price:\n\n>>> "))

        if not self._confirm(new_product):
            return True

        self.data_controller.products.create(**new_product)
        return True

    def update_product(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        product = self.data_controller.products.get(choice - 1)
        new_product = self._prompt_update(product.__dict__)
        if not self._confirm(new_product):
            return True

        product.update(**new_product)
        return True

    def delete_product(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        if not self._confirm():
            return True

        self.data_controller.products.delete(choice - 1)
        return True

    @staticmethod
    def exit_menu() -> bool:
        return False

    def _prompt_choice(self) -> int:
        self.print_products()
        print("0) Cancel\n")
        return self.select(self.data_controller.products)
