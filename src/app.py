import os

from rich.console import Console

console = Console()


class Menu:
    def __init__(self, options) -> None:
        self.options = options

    def loop(self):
        while True:
            self.print_menu()
            cmd = self.prompt()
            if cmd not in self.options.keys():
                if cmd == "0":
                    os.system("clear")
                    break

                os.system("clear")
                console.print("Invalid Option!\n", style="yellow")
                continue

            os.system("clear")
            self.options[cmd]()
            os.system("clear")

    def print_menu(self):
        for cmd, opt in self.options.items():
            if callable(opt):
                opt = opt.__name__.replace("_", " ").title()

            console.print(f"{cmd}) {opt}")
        console.print(f"0) Return")

    @staticmethod
    def prompt():
        return console.input("[yellow]>>>[/yellow] ")


class MainMenu(Menu):
    def __init__(self) -> None:
        self.options = {
            "1": self.manage_orders,
            "2": self.manage_products,
            "3": self.manage_couriers,
        }
        super().__init__(self.options)

    @classmethod
    def run(cls):
        main_menu = cls()
        main_menu.loop()
        console.print("Exiting Application...", style="red")

    def manage_orders(self):
        menu = OrderMenu()
        menu.loop()

    def manage_products(self):
        menu = ProductMenu()
        menu.loop()

    def manage_couriers(self):
        menu = CourierMenu()
        menu.loop()


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

    def get_products(self):
        pass

    def add_product(self):
        pass

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

    def get_couriers(self):
        pass

    def add_courier(self):
        pass

    def update_courier(self):
        pass

    def delete_courier(self):
        pass


if __name__ == "__main__":
    MainMenu.run()
