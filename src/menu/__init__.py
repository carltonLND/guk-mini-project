from .couriers import CourierMenu
from .menu import Menu
from .orders import OrderMenu
from .products import ProductMenu


class MainMenu(Menu):
    """Collection of responsibilities for the main menu interface"""

    _OPTIONS = ("Order Menu", "Product Menu", "Courier Menu", "Exit Application")

    def __init__(
        self, orders: OrderMenu, products: ProductMenu, couriers: CourierMenu
    ) -> None:
        self.commands = {
            1: self.goto_orders,
            2: self.goto_products,
            3: self.goto_couriers,
            0: self.exit_app,
        }

        self.order_menu = orders
        self.product_menu = products
        self.courier_menu = couriers

    def goto_orders(self) -> bool:
        self.order_menu.loop()
        return True

    def goto_products(self) -> bool:
        self.product_menu.loop()
        return True

    def goto_couriers(self) -> bool:
        self.courier_menu.loop()
        return True

    @staticmethod
    def exit_app() -> bool:
        return False
