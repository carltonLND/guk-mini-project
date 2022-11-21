class Product:
    def __init__(self, name: str, price: float, id: int | None = None) -> None:
        self.name = str(name)
        self.price = float(price)
        if id == None:
            self.id = id
        else:
            self.id = int(id)
