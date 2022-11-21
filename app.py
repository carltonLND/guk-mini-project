#!/usr/bin/env python3
"""CLI menu interface for a pop-up coffee shop management system"""

import typer

from src.cli_menu import courier_app, order_app, product_app

app = typer.Typer()

app.add_typer(product_app, name="products")
app.add_typer(courier_app, name="couriers")
app.add_typer(order_app, name="orders")


if __name__ == "__main__":
    app()
