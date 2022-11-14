from .menu import Menu


class CourierMenu(Menu):
    """Menu for interfacing with couriers"""

    _OPTIONS = (
        "Display Couriers",
        "Add New Courier",
        "Update Existing Courier",
        "Delete Courier",
        "Return",
    )

    def __init__(self, data_controller) -> None:
        self.commands = {
            1: self.print_couriers,
            2: self.add_courier,
            3: self.update_courier,
            4: self.delete_courier,
            0: self.exit_menu,
        }
        super().__init__(data_controller)

    def print_couriers(self) -> bool:
        print(self.data_controller.couriers)
        return True

    def add_courier(self) -> bool:
        new_courier = {}
        new_courier["name"] = input("Courier name:\n\n>>> ")
        new_courier["phone"] = int(input("Courier phone:\n\n>>> "))

        if not self._confirm(new_courier):
            print("No changes made\n")
            return True

        self.data_controller.couriers.create(**new_courier)
        return True

    def update_courier(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        courier = self.data_controller.couriers.get(choice - 1)
        new_courier = self._prompt_update(courier.__dict__)
        if not new_courier:
            print("No changes made\n")
            return True

        if not self._confirm(new_courier):
            print("No changes made\n")
            return True

        courier.update(**new_courier)
        return True

    def delete_courier(self) -> bool:
        choice = self._prompt_choice()
        if not choice:
            return True

        if not self._confirm():
            print("No changes made\n")
            return True

        self.data_controller.couriers.delete(choice - 1)
        return True

    @staticmethod
    def exit_menu() -> bool:
        return False

    def _prompt_choice(self) -> int:
        self.print_couriers()
        print("0) Cancel\n")
        return self.select(self.data_controller.couriers)
