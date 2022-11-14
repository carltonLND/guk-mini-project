from os import stat

from db import ABCDataController

from .menu import Menu


class OrderMenu(Menu):
    """Menu for interfacing with orders"""

    _OPTIONS = (
        "Display Orders",
        "Add New Order",
        "Update Order Status",
        "Update Order",
        "Delete Order",
        "Return",
    )

    def __init__(self, data_controller: ABCDataController) -> None:
        self.commands = {
            1: self.print_orders,
            2: self.add_order,
            3: self.update_order_status,
            4: self.update_order,
            5: self.delete_order,
            0: self.exit_menu,
        }

        super().__init__(data_controller)

    def print_orders(self) -> bool:
        print(self.data_controller.orders)
        return True

    def add_order(self) -> bool:
        if self.data_controller.products.empty():
            print("No products available\n")
            return True

        if self.data_controller.couriers.empty():
            print("No couriers available\n")
            return True

        new_order = {}
        new_order["name"] = input("Client name:\n\n>>> ")
        new_order["address"] = input("Client address:\n\n>>> ")
        new_order["phone"] = int(input("Client phone number:\n\n>>> "))
        new_order["courier"] = self._prompt_courier()
        new_order["items"] = self._prompt_items()
        if not self._confirm(new_order):
            return True

        self.data_controller.orders.create(**new_order)
        return True

    def update_order_status(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        order = self.data_controller.orders.get(choice - 1)
        status_list = self.data_controller.orders.status_list
        status = self._prompt_update_status(order, status_list)
        if not status:
            return True

        if not self._confirm():
            return True

        order.update_status(status_list[status - 1])
        return True

    def update_order(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        order = self.data_controller.orders.get(choice - 1)
        new_order = self._prompt_update(order.__dict__)
        if not self._confirm(new_order):
            return True

        order.update(**new_order)

        return True

    def delete_order(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        if not self._confirm():
            return True

        self.data_controller.orders.delete(choice - 1)
        return True

    @staticmethod
    def exit_menu() -> bool:
        return False

    def _prompt_choice(self) -> int:
        self.print_orders()
        print("0) Cancel\n")
        return self.select(self.data_controller.orders)

    def _prompt_courier(self) -> int:
        couriers = self.data_controller.couriers
        print(couriers)
        print("0) None\n")
        courier = self.select(couriers)
        if not courier:
            print("WARNING: no courier selected!\n")

        return courier

    def _prompt_items(self) -> list[int]:
        print(self.data_controller.products)
        print("0) Done\n")
        items = []
        while True:
            item_id = self.select(self.data_controller.products)
            if not item_id:
                break
            items.append(item_id)

        if not items:
            print("WARNING: no items in order\n")

        return items

    def _prompt_update(self, data: dict) -> dict:
        new_columns = {}
        for column in data.keys():
            match column:
                case "status" | "status_list":
                    continue
                case "courier":
                    new = self._prompt_courier()
                    if not new:
                        continue
                    new_columns[column] = new
                case "items":
                    new = self._prompt_items()
                    if not new:
                        continue
                    new_columns[column] = new
                case _:
                    new = input(f"New {column}:\n\n>>> ")
                    if not new:
                        continue
                    new_columns[column] = new

        return new_columns

    def _prompt_update_status(self, order, status_list) -> int:
        order.print_status_list(status_list)
        print("0) Cancel\n")
        return self.select(status_list, option_0=False)
