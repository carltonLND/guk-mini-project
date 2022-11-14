"""CLI menu interface for a pop-up coffee shop management system"""

import os
from pathlib import Path

from db import CourierList, CsvDataController, OrderList, ProductList
from file_handlers import CsvHandler
from menu import CourierMenu, MainMenu, OrderMenu, ProductMenu

DATA_DIR = os.path.join(Path(__file__).parent.parent, "data/")


def data_factory(data_dir) -> CsvDataController:
    """Factory that returns our constructed data controller"""
    handler = CsvHandler(data_dir=data_dir)
    orders = OrderList()
    products = ProductList()
    couriers = CourierList()
    return CsvDataController(
        handler=handler, orders=orders, products=products, couriers=couriers
    )


def menu_factory(data_controller) -> MainMenu:
    """Factory that returns our constructed main menu"""
    order_menu = OrderMenu(data_controller)
    product_menu = ProductMenu(data_controller)
    courier_menu = CourierMenu(data_controller)
    return MainMenu(order_menu, product_menu, courier_menu)


def main():
    """Setup and run cafe-cli"""
    data_controller = data_factory(DATA_DIR)
    data_controller.load()
    app = menu_factory(data_controller)
    app.loop()
    data_controller.save()
    print("Exiting Application!")


if __name__ == "__main__":
    main()
