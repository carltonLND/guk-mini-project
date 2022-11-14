from abc import ABC, abstractmethod


class ABCMenu(ABC):
    """Abstract interface for derived menu objects"""

    commands: dict

    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class Menu(ABCMenu):
    """Generic base class implementing recurring abstract methods"""

    _OPTIONS = ()

    def __init__(self, data_controller) -> None:
        self.data_controller = data_controller

    def loop(self) -> None:
        """Mechanism for the menu loop, if command returns True, continue"""
        print(self)
        choice = self.select()
        loop = self.commands[choice]()
        if loop == True:
            self.loop()
        return

    @property
    def options(self) -> tuple:
        """Tuple of str options available from the menu"""
        return self._OPTIONS

    def select(self, options=None, option_0=True) -> int:
        options = options or self._OPTIONS
        try:
            choice = int(input(">>> "))
        except ValueError:
            return self.select(options=options)

        if option_0:
            if 0 > choice or choice > (len(options) - 1):
                return self.select(options=options)
        else:
            if 0 > choice or choice > len(options):
                return self.select(options=options, option_0=False)

        return choice

    def _prompt_update(self, data: dict) -> dict:
        new_columns = {}
        for column in data.keys():
            new = input(f"New {column}:\n\n>>> ")
            if not new:
                continue

            new_columns[column] = new

        return new_columns

    def _confirm(self, data: dict = {}) -> bool:
        if data:
            for key, value in data.items():
                print(f"{key}: {value}")

        confirmation = input("\nConfirm? (Y|n)\n\n>>> ").lower()
        if confirmation == "n":
            return False

        return True

    def __len__(self):
        return len(self._OPTIONS)

    def __str__(self):
        string = ""

        num = 0
        for opt in self._OPTIONS:
            num += 1
            string += f"{num}) {opt}\n"

        return string.replace(f"{num}", "0")
