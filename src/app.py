#!/usr/bin/env python3
from menu import MenuController

if __name__ == "__main__":
    controller = MenuController.setup_factory()
    while True:
        controller.print()
        cmd = controller.current_menu.run()
        if not cmd:
            controller.prev_menu()
        else:
            controller.next_menu(cmd)
