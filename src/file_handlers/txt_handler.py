from file_handlers.handler import Handler


class TXTHandler(Handler):
    def load_data(self, file_name: str):
        with open(self.data_dir + file_name + ".txt", "r") as f:
            return f.read().splitlines()

    def save_data(self, file_name: str, data: list):
        with open(self.data_dir + file_name + ".txt", "w") as f:
            f.writelines(data)
