from rich import print as rprint


class Menu:
    def __init__(self, options) -> None:
        self.options = options

    def print_menu(self):
        rprint("Data:")
        for cmd, opt in self.options.items():
            if callable(opt):
                opt = opt.__name__.replace("_", " ").title()

            rprint(f"{cmd}) {opt}")


class MainMenu(Menu):
    def __init__(self) -> None:
        self.options = {
            "1": self.manage_orders,
            "2": self.manage_products,
            "3": self.manage_couriers,
            "4": self.exit_application,
        }
        super().__init__(self.options)

    def main_loop(self):
        pass

    def manage_orders(self):
        pass

    def manage_products(self):
        pass

    def manage_couriers(self):
        pass

    def exit_application(self):
        rprint("Exiting Application...")
        exit()


main = MainMenu()
main.print_menu()
