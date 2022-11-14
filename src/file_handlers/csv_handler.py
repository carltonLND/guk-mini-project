import csv
import os

from .handler import Handler


class CsvHandler(Handler):
    """Handler for csv file types"""

    ext = ".csv"

    def __init__(
        self,
        data_dir: str,
    ) -> None:
        self.data_dir = data_dir

    def load_file(self, filename: str) -> list[dict]:
        file = self.data_dir + filename + self.ext
        if not os.path.isfile(file):
            self._create_file(file)
            return []

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def save_file(self, filename: str, fieldnames: list[str], data: list) -> None:
        file = self.data_dir + filename + self.ext
        with open(file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in data:
                writer.writerow(obj.__dict__)
