#!/usr/bin/env python3
"""CLI menu interface for a pop-up coffee shop management system"""

import typer

from src.cli_menu import courier_app, order_app, product_app

app = typer.Typer(add_completion=False)

app.add_typer(
    product_app,
    name="products",
    help="Display a list of products when executed without an additional command.",
)
app.add_typer(
    courier_app,
    name="couriers",
    help="Display a list of couriers when executed without an additional command.",
)
app.add_typer(
    order_app,
    name="orders",
    help="Display a list of orders when executed without an additional command.",
)


if __name__ == "__main__":
    app()
