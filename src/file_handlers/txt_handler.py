class TXTHandler:
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def load_data(self, file_name: str):
        with open(self.data_dir + file_name, "r") as f:
            return f.readlines()

    def save_data(self, file_name: str, data: list):
        with open(self.data_dir + file_name, "w") as f:
            f.writelines(data)
