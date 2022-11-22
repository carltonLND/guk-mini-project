import csv
import os

CSV_DATA_PATH = "data/"


class CsvHandler:
    """Handler for creating, writing and reading csv files"""

    def __init__(self, filename: str, fieldnames: list[str]) -> None:
        self.fieldnames = fieldnames
        self.file = f"{CSV_DATA_PATH}{filename}.csv"
        if not os.path.isfile(self.file):
            open(self.file, "x").close()

    def load_file(self) -> list[dict]:
        """Returns csv data as list of dicts"""
        with open(self.file, "r") as f:
            return [row for row in csv.DictReader(f)]

    def save_file(self, data: list) -> None:
        """Saves data to file with selected fieldnames"""
        with open(self.file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for index, row in enumerate(data, 1):
                row.id = index
                writer.writerow(row.__dict__)
